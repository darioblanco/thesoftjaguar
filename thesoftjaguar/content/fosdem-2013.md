Title: FOSDEM 2013, it is more than beer
Date: 2013-03-08 20:02
Tags: conference, talk, FOSDEM, Brussels, Python
Category: programming
Slug: fosdem-2013
Summary: My thoughts about the FOSDEM event.

After my long blog hibernation, I wanted to write about *FOSDEM 2013*, which took place in Brussels on February 2nd and 3rd, and it wasn't only for drinking beer. OK, you got me, the beer is always a motivating factor.

![We share a dark past](http://i.imgur.com/Il4kdf4.jpg)


## The Virtualization alternative

The first day I was lost, the classrooms were really crowded, and I missed the Configuration Systems Management talk because, for "security purposes", nobody else could enter in the room. There is always a B Plan, so I attended some *Xen* talks about security using *Pygrub* and fixed kernels, explaining different attacks that can be performed to our virtual machines, some security practices like PV VMs or the Xen Security Module, and how to virtualizate in CentOS 6. It was nice to hear about all of this, because I am not really advanced in that issue.


## We should cook: Configuration Systems Management

However, Saturday afternoon was the Configuration Systems Management time. At that moment, I was aware of the overcrowding problem, so I arrived to the classroom 30 minutes earlier, and I spent the rest of the day there. From all the talks, I highlight these:

### Learning to Automate

This was a continuation of what I missed that morning, but the people were explaining their knowledge about certain *DevOps* practices, their experience with *Chef* and *Puppet* and how difficult can be sometimes. It was focused in how to debug your *Chef* cookbooks, introducing other projects like [Foodcritic](http://acrmp.github.com/foodcritic/) and [test-kitchen](https://github.com/opscode/test-kitchen). Of course, [Vagrant](http://www.vagrantup.com/) was the recommended method for testing your young cookbooks.

![We need a layered approach to Systems Management](http://i.imgur.com/bvFEbyM.jpg)

### Using Ruby frameworks to bring sanity to your infrastructure

*Vagrant* was over and over again, because it is a really interesting way of creating a development environment, so I wasn't surprised about how insistent they were about its use. But the main point here was that they explained some Ruby frameworks, and more important: their thoughts about each of them. I am not a Ruby expert so it was nice to know that *Cucumber* was not recommended at all, that *Rspec* have *Chefspec* and *Rspec-Puppet* as reference in this world, and a brief introduction to *Minitest* never hurts.

However, this talk was for explaining the *Test-Kitchen* project: useful for testing cookbooks across different operating systems, and capable of running the tests in Virtualbox or Openstack. Then you realize how complicated the testing of Configuration Management Systems can be, but possible after all.

Besides all of this, other libraries were meant, like *Celulloid*, *Bats* (Bash automated testing system), *Chef-Workflow*, *Berkshelf*, *Apache Mesos*, *Faraday*, *Sinatra*, *Rspec-dns*, *Ruby-dns* and more... That was all the libraryfest for the day.

### VeeWee

I enjoyed this one because it was a surprise talk (though I didn't love why it became a surprise). It was awesome to know more about the [VeeWee](https://github.com/jedi4ever/veewee) project and I definitely recommend it if you want to create almost any virtual machine in a really easy way.

![One does not simply choose the right kind of beer](http://i.imgur.com/Xrv3xC0.jpg)


## It's Python time

Sunday was the Python day, an overcrowded room as on Saturday but I could manage to pick a nice seat. The first talk was *Astonishing Python tricks*, a short one but explaining some Python particularities and putting together several Python patterns that the community have been using. Besides this, there are other talks that I want to highlight:

### Gaffer - Application deployment, monitoring and supervision made simple

I was skeptic about [Gaffer](http://gaffer.readthedocs.org/), but I am going to give it a try. At first I thought that it was like a distributed supervisor but it is more than that. I can think in a lot of uses for a company environment, and I am planning an open source project using this library.

### Plone, the best python-based CMS

[Plone](http://plone.org/) seems a really mature Python CMS. The security was his strongest point (and Python :P) but the weakest one was the deployment (as expected). If you really want to deploy even the most basic application, and you are not familiar to the basic concepts (and some other not as basics), is going to be difficult. They acknowledged those problems, but I have to say that as a CMS solution seems a really interesting one, if you can overcome the drawbacks. In my case, I am a control maniac, so that's why I prefer microframeworks like *Flask*, other not as micro as *Django*, and I intend to flee from CMS, though sometimes are really useful for certain situations.

### TDD from scratch

We love *Test Driven Development*, and if not, you should. Sometimes is hard, really hard, to program the test, because we are lazy. But then, with the experience, you realize that if we would have programmed a test at first, everything would have been easier. This talk addressed all the benefits of that philosophy change, and what tools we can use for easing the process.

### Vaurien the Chaos TCP Proxy

Based on Netflix Chaos Monkey project, [Vaurien](http://vaurien.readthedocs.org/) seems an useful way for testing distributed systems (and yeah, distributed systems need a lot of testing). Having a proxy between your code and any other system, in which you can put different protocols and behaviors, seems a really good approach for it. I am currently doing some testing actions with mock, and I think that *Vaurien* could solve them easily , so giving this project a try wouldn't be a bad idea.

### Python for Humans

My favorite talk, because it was a constructive Python critic, with the open source mind as a solution to all of its problems. I don't have to add much more because the slides are easy to be [found](https://speakerdeck.com/kennethreitz/python-for-humans). By the way, I also loved the [The Hitchhiker’s Guide to Python](http://python-guide.org)</a> project, I think that anyone who wants to get started with Python should take a look at it.

### How do event loops work in Python?

I love Asynchronous Programming, and I love how stupid I feel when I am dealing with it. In this talk, the [pyuv](http://pyuv.readthedocs.org) was introduced, and it seems really promising. It can be integrated with Twisted and Tornado. Besides that, there was an explanation and comparison of the different event loop libraries.

![Believe it or not, this place was an important piece of FOSDEM 2013](http://i.imgur.com/pWQSUZk.jpg)