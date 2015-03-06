Title: Sublime 3 and Python
Date: 2014-03-04 15:26
Tags: sublime, python
Category: programming
Slug: sublime3-and-python
Summary: How to set up a nice Python environment with Sublime Text 3.

This blogpost is a continuation from [Useful Sublime Packages](|filename|/useful-sublime-packages.md). The old one recommends outdated packages and I am not using Sublime Text 2 anymore, I switched to Sublime Text 3.

Though Sublime 3 is still on beta, I find it pretty mature, faster, with easier configuration, a lot of nice packages and filling all my development needs. It was a pretty easy choice for me.

# Setting up Sublime Text 3 & Package Control

Just download and install [Sublime Text 3](http://www.sublimetext.com/3) from their webpage.

Now you need to install [Sublime Package Control](https://sublime.wbond.net/installation). My prefered way is from `View > Show Console` or ``ctrl+` ``, were you can paste the following code in the built in console:

    :::python
    import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

![Install Sublime Package Control through the console](http://i.imgur.com/bw3dSmf.png)

# Install the desired packages

Installing any package [listed in Package Control](https://sublime.wbond.net/browse) is really easy. Just open the `Command Pallete` with `ctrl+shift+p` (Windows, Linux) or `cmd+shift+p` (OS X). All Package Control commands begin with the `Package Control:` prefix.

For installing a new package just select `Package Control:Install Package` (is faster to type `Install` and see how Sublime gets the full command for you), and type the package name there.

I can recommend a lot of packages but I want to highlight the ones that I think are essential.

## Anaconda, the ultimate Python package

I really like [Anaconda](https://github.com/DamnWidget/anaconda), it includes autocompletion, goto definitions, find usages, refactoring, code complexity checker, PyFlakes + PEP8 linting (can be switched to PyLint), among other interesting features.

![PEP8 error](http://i.imgur.com/kLmx1Eg.png)

It has everything I need for developing with Python, and I don't have to install different packages for achieving the same goal (like SublimeJEDI, SublimeLinter, etc...), it already brings those features.

![Autocomplete](http://i.imgur.com/Uur7egH.png)

### Goto Definition

You can follow the definition of any variable, function or class through all the project files. Really useful when calling another modules.

Shortcut: Linux `super+g`, Mac OS X and Windows `ctrl+alt+g`.

### Find usages

You can check how many times a function, variable or class has been used in the current file.

Shortcut: Linux `super+f`, Mac OS X and Windows `ctrl+alt+f`.

![Find usages](http://i.imgur.com/p7QfhpA.png)

### Get Documentation

If you need to get the docstring of any function or method, you just have to set the cursor on the function call and use the get docummentation command to obtain a function signature and docstring.

Shortcut: Linux `super+d`, Mac OS X and Windows `ctrl+alt+d`.

![Get Documentation](http://i.imgur.com/wiBVSkb.png)

You can always change Anaconda's default parameters and browse the README if you want to play more with it in `Package Settings`.

![Anaconda Package Settings](http://i.imgur.com/p0r0v6E.png)

Or just open the `Command Pallete` like before (when installing the Package Manager) and see all the available commands starting with `Anaconda:`.

## GitGutter, git changes in your editor

[GitGutter](https://github.com/jisaacks/GitGutter) will show you the lines in the opened file that are added, modified or deleted, based on the `git diff` command for your current repository.

![GitGutter](http://i.imgur.com/4WYUWKj.png)

## Monokai Extended, more syntax highlighting

This is not actually Python related, but [Monokai Extended](http://i.imgur.com/wiBVSkb.png) is really handy for other file types, for instance, Markdown, which was used for creating this blog post.

I also have the following optional color scheme setting:

    :::python
    {
        "color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme"
    }

# Change your settings

Sublime defines *default settings* and *user settings*. The settings are simple Python dictionaries. If you want to change a default setting, the recommended way is to override that entry in the user settings, so you can see easily what is special about your Sublime environment. If you respect the Python dictionary syntax, you will be fine.

![Settings User](http://i.imgur.com/J73rWAn.png)

You can see a full copy of my user settings [here](https://github.com/sharkerz/myconfig/blob/master/configs/Preferences.sublime-settings).

### Handle tabs and spaces

The default settings are not really Python friendly, if we follow PEP8 guidelines. In this case, I set up two user settings elements:

    :::python
    {
        "translate_tabs_to_spaces": true,  # Always use spaces!
        "draw_white_space": "all"  # Show spaces and tabs in the editor
    }

The most important is `"translate_tabs_to_spaces": true`, because we should always use spaces. In addition, some people can find `"draw_white_space": "all"` annoying , but for me, being able to see the white spaces and the tabs is really important because I'm a mess, and I most probably will put a tabulator without noticing it.


![Tabs and white spaces visualization](http://i.imgur.com/0pt1qow.png)

### Limit your line length

Even if Anaconda is going to show a PEP8 error if the line exceedes the code standard, another useful setting is to establish a ruler, for limiting the size of the code line.

    :::python
    {
        "rulers": [79],
        "wrap_width": 80
    }

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

In addition, I usually split the view in two columns, so it is better to compare code and I find myself more productive. You can do that in `View > Layout > Columns:2` or with `alt+cmd+2`.

![Two Columns view](http://i.imgur.com/0wjOIus.png)

# Organize your projects

I always use the following flow when there are no open files (that means all the projects are initially closed).

1. `Project > Add Folder to Project` and select the main folder.
2. `Project > Save Project As` and save it wherever you want (I have a folder called `SublimeProjects` for holding these files, but the location is not important, Sublime will store the links itself).
3. Once a Project has been opened, it will be displayed in `Project > Quick Switch Project` (or `ctrl+cmd+p` as a shortcut). From now on, you can use this quick switch for changing your project fast.

![Quick Switch Project](http://i.imgur.com/45HZjNz.png)
