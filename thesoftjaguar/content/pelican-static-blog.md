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

1. **Speed.** The parse is made once locally, and then the static pages are uploaded to the web root, ready to be served.
2. **Portability.** Your source blog pages are going to be written in a markup language like Markdown, Textile or Restructured Text, so we don't care about the design, and can be reused in other static blog engines, or even in other systems.
3. **Security.** It is the strongest point, everything is static, no server side code, no headaches.
4. **Configurability.** They usually have a configuration file, and you can create your own themes in a really easy way, using different template languages.
5. **Power.** *Git* power can be applied to the static blogs, tracking the changes in each blog post and using post-hooks for deploying both in *github* or in another web server. Forget about WYSWYG and complex admin interfaces: just use markup language, your favorite text editor and your preferred version control system, and you will be happy.
6. **Cheap.** You actually don't need expensive hosting, you can upload your static content to *github* and it will serve it for you.

Maybe the most famous static blog generator is [Jekyll](https://github.com/mojombo/jekyll) (Ruby), but I have enough Ruby when I program with Chef, so I wanted a Python alternative. I tried two: [Nikola](http://nikola.ralsina.com.ar/) and [Pelican](http://docs.getpelican.com/).

My colleague [Aengus Walton](http://ventolin.org/) has been migrating his Wordpress blog to a static blog philosophy, and for that purpose he recommends Nikola over Pelican, it seems that Nikola handles Wordpress in a better way. I have to say that Nikola is a great alternative, but in my specific case, I decided to use Pelican for this purpose.


## Why Pelican

With Nikola I had some issues when customizing the blog, so instead of trying to figure out what was going on, I decided to try Pelican.

For me Pelican has everything that I need: comments with Disqus, themes using Jinja2, syntax hightlighting, feeds, Twitter and Google Analytics integration, and publication of articles in multiple languages.

Actually this last point was one of the reasons why I tried Pelican: I thought that it wasn't supporting multilanguage (Nikola does). I didn't have any problem with Pelican in the process, and everything was astonishingly easy, so I didn't consider any other alternative after such a nice experience.


## The process

### Initializiting the project

I always recommend using `virtualenv` and `virtualenvwrapper`, and then install the required `pip` packages inside the virtual environment. In this case I am using `markdown` as a markup format for my blog post, so I am installing it as well:

    :::bash
    $ mkvirtualenv my-pelican-blog -a ~/my-pelican-blog-project-folder
    $ pip install -r pelican markdown

Once you have set up your virtual environment, the cool part begins. Just run the `pelican-quickstart` command, and answer each question:

    :::bash
    $ pelican-quickstart

That's going to create the project layout, putting each blogpost markdown file in the `content` folder. Running the following command will generate the static HTML files with Pelican's simple theme:

    :::bash
    $ make html

And well, of course you want to check how the blog is looking like:

    :::bash
    $ make serve

### Defining Pelican settings

Now you will see two new files, `pelicanconf.py` and `publishconf.py`. They are settings files, filled with the answers that you gave running `pelican-quickstart`. In my specific case, I tuned them up a bit, for matching my personal requirements.

First of all, I wanted to set *DISQUS* as external comment system:

    :::python
    DISQUS_SITENAME = "thesoftjaguar"

I also wanted to arrange the post urls by date, for handling `archives` later:

    :::python
    # Urls
    ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
    ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
    YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
    MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

I activated the feeds for all the posts, categories and tags:

    :::python
    # Feeds
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    FEED_ALL_RSS = 'feeds/all.rss.xml'
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
    CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
    TAG_FEED_ATOM = 'feeds/%s.atom.xml'
    TAG_FEED_RSS = 'feeds/%s.rss.xml'

I also had some static pages that were not going to be generated by Pelican, so it has to know that we want to parse them as well:

    :::python
    TEMPLATE_PAGES = {
        'projects.html': 'projects.html',
    }

Finally, I decided to implement my own theme, using *Twitter Bootstrap*. Pelican will check in different places for a folder match, and then it will parse the content from that theme folder:

    :::python
    THEME = 'bootstrap-theme'

### Creating your own theme

If you want some extra customization (like I do), you will create your own theme. [Pelican themes](https://github.com/getpelican/pelican/tree/master/pelican/themes) are quite cool, but I already had a really basic page using *Twitter bootstrap* and I wanted to adapt my old Django blog to that style.

A way of doing this, is to create a folder with your theme name, as it is defined in the `THEME` setting parameter. In my case I called my theme `bootstrap-theme`, with two other folders: `static` and `templates`. Pelican is requiring a specific [folder structure](http://docs.getpelican.com/en/3.1.1/themes.html#structure).

I copied [simple theme](https://github.com/getpelican/pelican/tree/master/pelican/themes/simple/templates) template files into my `templates` folder, and I editted them. In addition, there is a cool feature in Pelican 3: if it doesn't find a required template file, it will inherit it from the `simple` theme, so you don't need to store uneditted simple theme files in your custom theme.

Now, you are on your own. You should keep in mind that there are several [template variables](http://docs.getpelican.com/en/3.1.1/themes.html#templates-and-variables) that you have to use, but that's it.

However, I found several problems when I wanted to display the blog archives by year and month, and Pelican's documentation is not really clear about that subject. Using Jinja2 `groupby` filter was my way of solving the problem:

    :::jinja
    <h1 class="page-title">Archive</h1>
    <ul>
        {% for year, year_articles in articles|groupby('date.year') %}
        <li><h2>{{ year }}</h2></li>
        {% for month, month_articles in year_articles|groupby('date.month') %}
        <ul>
            <li><h4>{{ month_articles[0].date.strftime('%B') }}</h4></li>
                {% for article in month_articles %}
                <div class="entry-archive">
                    <div class="date">
                        {{ article.date.strftime('%A %d') }}
                    </div>
                    <div class="detail">
                        <a href="{{ SITEURL }}/{{ article.url }}" rel="bookmark" title="Permalink to {{ article.title|striptags }}">{{ article.title }}</a>
                    </div>
                </div>
                {% endfor %}
        </ul>
        {% endfor %}
        {% endfor %}
    </ul>

### Writing your first article

Just create a `.md` file in the `content` folder, and write the metadata, followed by the actual Markdown formatted text:

    :::html
    Title: Migrating to a Pelican static blog
    Date: 2013-04-06 02:24
    Tags: static-blog, markdown, pelican, python, web-development, git, django
    Category: programming
    Slug: pelican-static-blog
    Summary: How did I migrate my Django blog to a static one, using Pelican.

    This is the content of my blog post. I should use Markdown here.

Save the file, run `make html`, and that's it.

### Deploying to your web server

I have my Pelican project, [thesoftjaguar](https://github.com/sharkerz/thesoftjaguar), on Github. However, I don't intend to serve the static files there, because I already have a personal web server.

I am using a git post-hook to my personal web server, as explained in [Deploying applications with git](|filename|deploying-applications-with-git.md), so I have two remotes in my `thesoftjaguar` repository: github and my personal server. But the `post-receive` hook is going to be a bit different, because I only want to serve the `output` folder:

    :::bash
    TMP_GIT_REPO=/home/dario/git/tmp/thesoftjaguar
    WEB_ROOT=/home/dario/www

    GIT_WORK_TREE=$TMP_GIT_REPO git checkout -f
    GIT_WORK_TREE=$TMP_GIT_REPO git reset --hard
    rm -rf "$WEB_ROOT/*"
    cp -r "$TMP_GIT_REPO/thesoftjaguar/output/*" $WEB_ROOT

And now we add the new remote:

    :::bash
    $ git remote add web dario@darioblanco.com:git/thesoftjaguar.git

For now on, the deployment is totally independent from the github repo, and is going to be extremely comfortable:

    :::bash
    $ git push web master