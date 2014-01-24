thesoftjaguar
=============

My static blog, created with Pelican

Create pygments css file
> $ pygmentize -S default -f html > pygments.css

The site is now managed using `fabric`. Just install all the dependencies:
> $ pip install -r requirements.txt


## Manage with fabric

This is the recommended way.

Generate the site
> $ fab build

Regenerate the site everytime a change is detected
> $ fab regenerate

Serve locally
> $ fab serve

Deploy to the desired server through SSH. The config is in `secret.py`, please rename the `secret.py.example` file.
> $ fab publish


## Manage with make

I don't use this method anymore.

Publish html
> $ make html

Serve locally
> $ make serve

Upload to your remote server (if your remote is called `web`)
> $ git push web master
