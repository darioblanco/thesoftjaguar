Title: Migrating to a Pelican static blog
Date: 2013-04-06 02:24
Tags: static-blog, markdown, pelican, python, web-development, git, django
Category: programming
Slug: pelican-static-blog
Summary: How did I migrate my Django blog to a static one, using Pelican.

In October 2011, as a Django training exercise, I decided to develop a blog engine from scratch, and I called it [blogjaguar](https://github.com/sharkerz/blogjaguar). It was quite interesting and I had a lot of fun in the process, but it wasn't easy and updating it required a lot of time, even if the web framework was making the things easier. That's why I have decided to drop its support, and migrate to a static blog, integrating it with a basic bootstrap webpage that I had for my personal portfolio.


## The static blog concept

Instead of having a server side application which is going to parse the client request given by the web server, compile a template based on the given data (this step can be avoided sometimes with a cache system), and return it as an HTML page, we simply skip the first two steps, serving the static HTML page directly, without any programming language as a proxy.

And there are many questions... How? We don't really need an admin interface for writing a blog post: we can do it directly creating another HTML page. We don't need our own comment system, we can include an external one like *Disqus*. We don't need to register users in our page, they don't want to register in a blog. There are many tasks that we can do without creating the HTML pages dynamically.

Fine, now you are thinking that this is a mess, why should you be editting the HTML pages every time you want to create a new blog entry? It seems easier with an administration panel and a WYSWYG editor. And that's why we have static blog generators. 


## The static blog generator

There are many static blog generators, and they provide a really interesting set of features:

1. Speed: the parse is made once locally, and then the static pages are uploaded to the web root, ready to be served.
2. Portability: your source blog pages are going to be written in a markup language like Markdown, Textile or Restructured Text, so we don't care about the design, and can be reused in other static blog engines, or even in other systems.
3. Security: it is the strongest point, everything is static, no server side code, no headaches.
4. Configurability: they usually have a configuration file, and you can create your own themes in a really easy way, using different template languages.
5. Power: *git* power can be applied to the static blogs, tracking the changes in each blog post and using post-hooks for deploying both in *github* or in another web server. Forget about WYSWYG and complex admin interfaces: just use markup language, your favorite text editor and your preferred version control system, and you will be happy.
6. Cheap: you actually don't need expensive hosting, you can upload your static content to *github* and it will serve it for you.

Maybe the most famous static blog generator is [Jekyll](https://github.com/mojombo/jekyll) (Ruby), but I have enough Ruby when I program with Chef, so I wanted a Python alternative. I tried two: [Nikola](http://nikola.ralsina.com.ar/) and [Pelican](http://docs.getpelican.com/).

My colleague [Aengus Walton](http://ventolin.org/) has been migrating his Wordpress blog to a static blog philosophy, and for that purpose he recommends Nikola over Pelican, it seems that Nikola handles Wordpress in a better way. I have to say that Nikola is a great alternative, but in my specific case, I decided to use Pelican for this purpose.


## Why Pelican


## The process

### Initializiting the project

### Defining Pelican settings

### Creating your own template

### Writing your first article

### Parsing the html

### Deploying to your web server

