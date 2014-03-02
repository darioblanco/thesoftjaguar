

This blogpost is a continuation from the old one, regarding Sublime Text 2.

Download Sublime 3
http://www.sublimetext.com/3

Install Sublime Package Control
https://sublime.wbond.net/installation

View > Show Console

`import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)`

Now we will proceed installing the packages.

Command + Shif + P

Package Control: Install Package

Anaconda

GitGutter



-- My preferred settings

-- Goto definition and Find Usages

-- Get documentation

-- How to Organize Projects

-- Vagrant integration
