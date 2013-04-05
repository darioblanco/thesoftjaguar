Title: Hackathon project: Jenkins is calling
Date: 2012-09-04 18:59
Tags: hackathon, Jenkins, continuous-integration, Android, Java, Websocket, asynchronous, Tornado
Category: hackathon
Slug: jenkins-is-calling
Summary: A one day project for annoying the developer whenever the scheduled Jenkins build is broken, and for annoying him a bit more when it is finally fixed.


## What is a Hackathon?

In the company I work for, [edelight](http://www.edelight.de/), we have Hackathon days. The idea is to team up with colleagues and work on a project of your choice for one entire day. There are no limitations on what you want to do and at the end of the day you have to present a prototype to all the team. So the last Hackathon was in July and there were a lot of interesting projects, you can always check what is happening in our [team blog](http://labs.edelight-group.com/).

## Having fun with Jenkins

We have a continuous integration server using [Jenkins](http://jenkins-ci.org/), with a post-hook to our github repos for tracking the master branch on every project. It is really important for checking if the build is failing in the staging server, and it helps a lot in terms of code quality.

In my case, I decided to create a really basic Android application, showing an annoying window with a silly background music whenever the Jenkins build is red (failing), or when is switching from the red state to blue (fixed).

## A technical approach

In order to have an asynchronous communication, the Android application is implementing a [WebSocket](http://tools.ietf.org/html/rfc6455) Java client, subscribed to a [Tornado](http://www.tornadoweb.org/en/stable/) application that implements the WebSocket server. If you are a bit scared about Tornado, please don't, it is quite easy to create a [WebSocket server](http://www.tornadoweb.org/en/stable/websocket.html?highlight=websockets).

![Android app main view](http://i.imgur.com/SFpfb.png)

## The push notification

Once the client is subscribed, every time a Jenkins build is changing its status to `failing` or `fixed`, the Tornado app will know it and will send a broadcast message (push message) to all the suscribers. In that case, the Android client (even if it is in sleeping mode), will populate the Activity window in front of all the ones that you had opened before, and an awesome music (copyright free of course) will be played.

## The build is failing ¬¬

When a new commit is pushed into master, Jenkins runs the project tests, code coverage, pep8, pylint... If something is wrong, the build will fail. In that case, the mobile phone will display the TROLOLO window, with the [TROLOLO song](http://youtu.be/ednKK8GlvwI).

## The build is fixed ^^

Of course, if the build is failing, someone has to fix it. If a benevolent soul has commited the patch fix into master, Jenkins will pass all the tests again, and it will stop spamming our email accounts. The way in which it stops the spam is quite funny: sending a last email message saying that it is fixed.

However, I thought that the spam wasn't enough, so in that case, your mobile phone will also display the KEYBOARD CAT window, and the [KEYBOARD CAT song](http://youtu.be/J---aiyznGQ) as a token of victory.

## Life's for sharing

You can browse the code on [github](https://github.com/sharkerz/jenkins-calling). I haven't had a lot of time for developing this, so I haven't cleaned the code a lot (and I'm sharing the client only), but if someone is really interested in it, you can always ping me in twitter or by email.