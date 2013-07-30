thesoftjaguar
=============

My static blog, created with Pelican

Create pygments css file
> $ pygmentize -S default -f html > pygments.css

Parse html
> $ make html

Serve locally
> $ make serve

Upload to your remote server (if your remote is called `web`)
> $ git push web master
