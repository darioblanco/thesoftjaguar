Title: Deploying applications with git
Date: 2012-02-29 16:33
Tags: Git, deployment, bare, non-bare, version control
Category: programming
Slug: deploying-applications-with-git
Summary: How to deploy easily your application using a git post-hook.

Usually, when we work with an application, especially with web applications, we wonder what is the best way for deploying it, and there are many. It is really important to be comfortable with the way in which we deploy these kind of applications, because the productivity is going to be strongly related to it. Here I explain some `git` basics, and how to easily configure it for updating automatically a specific folder (for instance, the web root folder) with the last pushed revision.

![Git trunk](http://thekevindolan.com/wp-content/uploads/2010/03/git_two1-600x480.jpg)

## Understanding the basics

Instead of copypaste the web app local content, or work directly on the server, we will have a distributed version control system like `git` to check every local changes (even if we want to work individually), with all the functionality that it provides. Therefore, every time a commit is made, it will not be in the remote server until we do the appropiate push. If you want to know more about `git` I recommend the following [cheatsheet](http://rogerdudler.github.com/git-guide/" target="_self).

For example, if we want to create a local repository (although it doesn't matter, it could be an existing one), we will write the following commands:

> $ mkdir webapp

> $ cd webapp

> $ git init

> Initialized empty Git repository in /home/user/webapp/.git/

> $ touch index.html

> $ git add index.html

> $ git commit -m "First commit"

## The bare and non-bare differentiation

Now we have a local `git` repository, but... What about the server? I'll try to be as generic as possible regarding the creation of the repository. In addition, I have to highlight the difference in `git` between bare repositories and non-bare repositories.

The bare repositories only have version control files and not work files (tree), also they don't include the special directory .git. Instead, it includes all of its content directly in the root of the bare repository. They are used to have a central repository where the developers can do pull and push: it is a correct way of doing this.

The non-bare repositories have a special folder `.git` which has the control version system information, and the work files: the tree. The local repository which we have created is non-bare.

## Working in the server

Therefore, the idea is to create a bare repository in the server, such that when it receives a push, it will upgrade the web app directory (the folder that we want, for instance, avoiding the change of other management folders, such as the one which contains apache server scripts). This repository will be a mirror from the local one:

> $ mkdir webapp.git

> $ cd webapp.git

> $ git init --bare

> Initialized empty Git repository in /home/user/webapp.git/

## The post-hook creation

We need to tell `git` to apply the changes in the desired folder, so we must define a post-hook who will apply the changes when the remote repository receives a push, doing a check-out of the last tree in the desired folder. Editing the post-receive file (in the &quot;hook&quot; folder from the bare repository) will do the trick:

> GIT_WORK_TREE=/home/user/target_dir git checkout -f

> GIT_WORK_TREE=/home/user/target_dir git reset --hard

If it was a Django project, we would have defined the project folder (the one with settings.py in it). Otherwise it could have been the `/var/www/example_webapp` folder, etc. We have to give execute permissions to the post-receive file (for example with the command `chmod +x hooks/post-receive`).

## Finishing the local set up

Back in the local repository, it will be necessary to define the remote repository name (the mirror) and create a master branch in it. For example, we will call the branch &quot;web&quot;.

> git remote add web username@domain.com:webapp.git

> git push web +master:refs/heads/master

We will have the `index.html` dummy file in the desired server folder. From now on, changes are made with the following command:

> $ git push web

The small inconvenience of setting up this, is worth the time.