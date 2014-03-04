Title: Sublime 3 and Python
Date: 2014-03-03 12:10
Tags: sublime, python
Category: programming
Slug: sublime3-and-python
Summary: How to set up a nice Python environment with Sublime Text 3.

This blogpost is a continuation from [Useful Sublime Packages](|filename|/useful-sublime-packages.md). The old one recommends outdated packages and I am not using Sublime Text 2 anymore, though Sublime 3 is still on beta, I find it pretty mature, faster, with easier configuration, a lot of nice packages and filling all my development needs.

# Setting up Sublime Text 3 & Package Control

Just download and install [Sublime Text 3](http://www.sublimetext.com/3) from their webpage for your platform.

However, you are not done yet, you need to install [Sublime Package Control](https://sublime.wbond.net/installation). There are many ways to do this, but my preffered one is just going to `View` > `Show Console` or `Ctrl` + ``` in Sublime Text and paste the following code there:

    :::python
    import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)


# Install the desired packages

Installing any package [listed in Package Control](https://sublime.wbond.net/browse) is really easy. Just open the Command Pallete with `Ctrl` + `Shift` + `P` (Windows, Linux) or `Cmd` + `Shift` + `P` (OS X). All Package Control commands begin with `Package Control:`, start by typing `Package ` so for installing a new package just type `Package Control:Install Package` and type the name there (is faster to type `Install` and see how Sublime gets the full command for you).

I can recommend a lot of packages but I want to highlight the ones that I think are essential.


## Anaconda, the ultimate Python package

I really like this package, it includes autocompletion, goto definitions, find usages, refactoring, code complexity checker, PyFlakes + PEP8 linting (can be switched to PyLint), among other interesting features.

![PEP8 error](http://i.imgur.com/kLmx1Eg.png)

![Find usages](http://i.imgur.com/p7QfhpA.png)

It has everything I need for developing with Python, and I don't have to install different packages for achieving the same goal (like SublimeJEDI, SublimeLinter, etc...), it already brings those features.


## GitGutter, git changes in your editor

GitGutter will show you the lines in the opened file that are added, modified or deleted, based on the `git diff` command for your current repository.

![GitGutter](http://i.imgur.com/4WYUWKj.png)


# Change your settings

Sublime defines default settings and user settings. The settings are simple Python dictionaries. If you want to change a default setting, the recommended way is to override that entry in the user settings, so you can see easily what is special about your Sublime environment.

![Settings User](http://i.imgur.com/J73rWAn.png)

### Handle tabs and spaces

The default settings are not really Python friendly, if we follow PEP8 guidelines. The most important is `"translate_tabs_to_spaces": true`, because we should always use spaces. In addition, I set up `"draw_white_space": "all"`, some people find it annoying, but for me, being able to see the white spaces and the tabs is really important because I am a mess, and I most probably will put a tabulator without noticing it.

![Tabs and white spaces visualization](http://i.imgur.com/0pt1qow.png)

### Limit your line length

Even if Anaconda is going to show a PEP8 error if the line exceedes the code standard, another useful setting is to establish a ruler, for limiting the size of the code line.

I am a bit strict with PEP8 in this case, and I set a ruler of 79 characters max with `"rulers": [79]`, but if you want to be more flexible (and actually PEP8 allows this flexibility), you can change the default Anaconda value as well.

Another useful setting is `"wrap_width": 80`, which will force wrapping at the column rather than the window width.

![Wrap width](http://i.imgur.com/2qc1mYg.png)

I do this because I like to split my Sublime layout in two columns, so I can browse two files and compare them if I need. Limiting the line following a code standar is really helpful for that.

### Ignore files from appearing in the sidebar

Here you can add the patterns that you want to ignore in the left side bar. This is just an example:

    ::python
    {
        "folder_exclude_patterns": [
            ".svn",
            ".git",
            ".DS_Store",
            "__pycache__"
        ]
    }

### Other settings

These are some stetic settings that I have set up:

    ::python
    {
        # Minimap shows the current position in the document
        "always_show_minimap_viewport": true,
        # Shows folders in the side bar in bold
        "bold_folder_labels": true,
        # Draws a border around the visible rectangle in the minimap
        "draw_minimap_border": true,
        # Avoids sending anonymised data to Sublime HQ
        "enable_telemetry": false,
        # Ensures that the last line of the file ends in newline when saving
        "ensure_newline_at_eof_on_save": true,
        # Makes tabs with modified files more visible
        "highlight_modified_tabs": true,
        # Draws indent guides containing the caret in a different color
        "indent_guide_options": [
            "draw_active",
            "draw_normal"
        ],
        # Adds whitespace up to the first open bracket when indenting
        "indent_to_bracket": true,
        # Avoids previewing file contents when clicking on a file in the side bar
        "preview_on_click": false,
        # Makes shift+tab always unindent, instead of inserting tabs
        "shift_tab_unindent": true,
        # Hides the Build Results panel when building
        "show_panel_on_build": false,
        # Removes trailing white space on save
        "trim_trailing_white_space_on_save": true,
    }


-- Goto definition and Find Usages

-- Get documentation

-- How to Organize Projects

-- Skins

-- 2 Column Layout

