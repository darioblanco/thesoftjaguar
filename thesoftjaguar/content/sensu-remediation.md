Title: Explaining Sensu remediation
Date: 2015-06-14 19:31
Tags: sensu, monitoring, distributed, cluster
Category: monitoring
Slug: sensu-remediation
Summary: How does Sensu remediation work? An overview of the remediator handler and how to trigger checks asynchronously from the API.

[Sensu](https://sensuapp.org/) is a great distributed monitoring system, and I love its flexibility. At [wywy](http://wywy.com/) we use Sensu for monitoring four datacenters in several countries (and overseas), with around 1300 checks issued every minute in 200 clients.

When you start having a big infrastructure, and so many checks in critical systems, something can go wrong, and the engineer has to fix it ASAP. Then you can observe how trivial is to fix some alerts, and how a script could do it automatically. But how to set up such script? Here is the concept of **remediation**: a special sensu check that runs a specific command for fixing the state of a triggered alert. For instance, a specific process is stopped, the sensu alert informs about that, thus the remediation triggers a process restart.

How do we achieve this behavior within sensu? We will need to address four different concepts: the standard check, the remediator handler, and the unpublished remediation check.

## The client configuration

It's worth mentioning each sensu host has a ``client.json`` config, and as the remediator will use the subscriptions list with the hostname, it is necessary to suscribe each host to its hostname (thanks Kenny Garland for the reminder).

Something like this in ``/etc/sensu/conf.d/client.json``:

```json
{
  "client": {
    "name": "myhost.foo.var.com",
    "address": "192.168.1.1",
    "subscriptions": [
      "myhost.foo.var.com"
    ],
    ...
}
```

## The standard check

In sensu, there are two ways of defining a standard check, server side, where the client has to subscribe to that check (via RabbitMQ) and will be triggered when the Sensu server asks for it, or client side, where the client defines the check as standalone and schedules it without needing a server trigger.

In order to apply remediation, you will need to set your remediate checks (not necessarily the actual alert check) as ``"standalone": false``. However, in this blogpost, I will also define the alert check as a server check, but you can try setting that one to standalone and will work as soon as the server evaluates the handler properly (I have never tried this and feel free to give output about it).

An example of server check config in ``/etc/sensu/conf.d/checks/check-zookeeper-proc.json``, that verifies if our zookeeper process is up:

```json
{
  "checks": {
    "check-zookeeper-proc": {
      "command": "/etc/sensu/plugins/check-procs.rb -p '/usr/share/java/zookeeper.jar'",
      "interval": 60,
      "occurrences": 2,
      "handlers": ["default"],
      "subscribers": ["zookeeper"]
    }
  }
}
```


## The remediator handler

When the client receives a check request from the server, it executes the given command, and sends back the output to the server. You can program special actions for evaluating that input given from the client, in the server: that's what the **handlers** do.

There are a lot of different sensu handlers (sending emails when the check is critical, send the events to external systems like PagerDuty or OpsGenie, etc...). For remedation, we have the [remediator handler](https://github.com/sensu/sensu-community-plugins/blob/master/handlers/remediation/sensu.rb), and yeah, maybe calling it ``sensu.rb`` wasn't the best idea as can be misleading in the handlers folder. Once you put that script in your sensu handlers folder (for instance ``/etc/sensu/handlers/sensu.rb``), you need to add the handler config to ``/etc/sensu/conf.d/handlers``.

An example of remediation handler config in ``/etc/sensu/conf.d/handlers/remediator.json``:

```json
{
  "handlers": {
    "remediator": {
      "command": "/etc/sensu/handlers/sensu.rb",
      "type": "pipe",
      "severities": ["critical"]
    }
  }
}
```

Remember our previous check example? Now you need to extend it for using the remediator handler! Take a look at the new fields, as you will need to extend the ``handlers`` field and add a new custom ``remediation`` field.

```json
{
  "checks": {
    "check-zookeeper-proc": {
      "command": "/etc/sensu/plugins/check-procs.rb -p '/usr/share/java/zookeeper.jar'",
      "interval": 60,
      "occurrences": 2,
      "handlers": ["default", "remediator"],
      "subscribers": ["zookeeper"],
      "standalone": false,
      "remediation": {
        "remediate-zookeeper-proc": {
          "occurrences": [1, 3],
          "severities": [2]
        },
      "trigger_on": ["zookeper"]
    }
  }
}
```

And this part is a bit tricky, as the ``remediation`` field is quite special.

First of all, the remediation handler will verify if the check output is having the specified severity, which in this case is 2 (CRITICAL), and you can specify a list of different severities if you wish, if the alert has one of the list, it will evaluate it.

Once the severity matches the expected one, the remediator will verify if the check occurrence is one of the defined in the config. In the example, remediation will work only in the first and third critical alert.

If you want to achieve a completely different behavior, like a range of occurrences, I recommend you to check the [source code](https://github.com/sensu/sensu-community-plugins/blob/master/handlers/remediation/sensu.rb)).


## The unpublished remediation check

There is still one more check needed, the unpublished one. This is a very special check, and is the one that **can't be a standalone check**. It can't be scheduled by the client because a ``published: "false"`` check can only be triggered by the Sensu API asynchronously, and is the whole trick that the remediation uses: the remediator handler will send to the Sensu API a check request, thus the Sensu API will activate it!

An example of unpublished remediation check config in ``/etc/sensu/conf.d/checks/remediate-zookeeper-proc.json``:
```json
{
  "checks": {
    "remediate-zookeeper-proc": {
      "command": "sudo supervisorctl restart zookeeper",
      "handlers": [],
      "subscribers": ["zookeper"],
      "standalone": false,
      "publish": false
    }
  }
}
```


## How does it work

This is how the whole remediation system works:

1. Sensu server publishes a check request for ``check-zookeeper-proc``.
2. Sensu client who was listening to ``zookeeper`` receives the request, runs the command and gives the output to the Sensu server.
3. Sensu server evaluates the handler list, discovering the ``default`` and ``remediation`` handler.
4. Sensu server runs the ``remediation`` handler with the output given, reads the different values, and if all the conditions pass, issues the remediate check via the API (POST request with the *check* and *subscribers* in the body).
5. Sensu client receives the check request from the Sensu API for ``remediate-zookeeper-proc`` and runs the remediation command.
