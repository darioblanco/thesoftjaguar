Title: My trip through RabbitMQ clustering, now with more turbulences
Date: 2014-06-18 17:12
Tags: rabbitmq, queue, erlang, distributed, cluster
Category: queue
Slug: rabbitmq-clustering
Summary: How to set up a RabbitMQ cluster with a Firewall behind and non dynamic Erlang epmd ports.

I actually wanted to create a small blogpost, just for once, for creating a *RabbitMQ* cluster. It looks easy, but can be tricky, even if you follow the [RabbitMQ Clustering Guide](https://www.rabbitmq.com/clustering.html). So yeah, first read the guide and then read my blogpost, I will cover the problems I found for creating the cluster here.


## The mnesia error

If you join the cluster like this:

```shell
  $ rabbitmqctl join_cluster --ram rabbit@ip-10-158-xxx-xxx
```

And you don't stop the application before doing that, you will have a nice error:

```
  Error: mnesia_unexpectedly_running
```

Is scary, but the fix is easy. Make sure you call `rabbitmqctl stop_app` before issuing the cluster command. Then make sure you call `rabbitmqctl start_app` to begin it again :)

## The dynamic Erlang ports

This one was the trickiest. The Erlang *epmd* (erlang port mapper daemon) will use two ports ,one for discovering other erlang nodes (port `4369`) and a **dynamic range** for the actual communication. And yes, *RabbitMQ* will use *epmd* for clustering, so I will refer from now to *epmd* only.

For two Erlang nodes to be able to communicate they:

- must have the same cookie, it identifies the Erlang cluster, so the cookie has to be the same in each cluster node. As *RabbitMQ* uses Erlang, you will see how important the cookie is, and **you should always check that the cookie is the same in every node when debbuging RabbitMQ clustering errors**.

- must be able to resolve the other node's hostname to an IP

- must be able to connect to the *epmd* on that IP (remember it listens on port 4369 by default for that kind of discovery)

- must be able to connect to the other node's distribution port. That
port is chosen dynamically (though you can "pin" it with `-kernel
inet_dist_listen_min 44001 inet_dist_listen_max 44001`) and returned by *epmd*.

What the hell? Dynamic range? Really? Come on guys, I have a firewall (the question is: who is not having a firewall?), and OBVIOUSLY I don't want to open a really big range of ports just for allowing lady Erlang to pick one each time. Of course, you can configure it for picking a small range (or even one port), and is easy in Erlang, but it wasn't obvious.

As a first step in tracking down the problem I suggest you start some
test Erlang nodes on all your machines with:

```shell
   erl -sname mytest -setcookie mycookie
```

But that command will create a port for communication with other Erlang ports in every invokation. An example command for setting a specific range of Erlang ports will be the following:

```shell
  erl -sname mytest -setcookie mycookie -kernel inet_dist_listen_min 44001 inet_dist_listen_max 44001
```

And yeah! There is a kernel parameter. For setting a specific range of ports in *epmd*, you have to specify kernel values. In the command we set 44001 as the *epmd* port for communication.

You can check where the epmd nodes are running, really useful for realizing if your RabbitMQ node is running where it should. An example generic command for that is the following:

```shell
  $ epmd -names
  epmd: up and running on port 4369 with data:
  name bar at port 30001
  name foo at port 30000
```

## RabbitMQ and how it sets the Erlang ports

This is not the end of your problems. *RabbitMQ* invokes Erlang itself, so you have to realize how in the damn hell does it set those kernel values to *epmd*.

Well, the answer is `rabbitmq.config`. You can follow the next example:
```
% Example of rabbitmq/templates/rabbitmq.config for clustering
[
  {rabbit, [
    {cluster_nodes, {['rabbit@mynode1', 'rabbit@mynode2'], disc}},
    {cluster_partition_handling, ignore},
    {default_user, <<"guest">>},
    {default_pass, <<"guest">>}
  ]},
  {kernel, [
    {inet_dist_listen_max, 44001},
    {inet_dist_listen_min, 44001}
  ]}
].
% EOF
```
