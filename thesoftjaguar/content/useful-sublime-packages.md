Title: Useful Sublime packages
Date: 2012-09-07 19:33
Tags: Sublime, editor, programming, plugins, packages
Category: programming
Slug: useful-sublime-packages
Summary: Brief explanation of Sublime Package Control, how to easily install plugins and a recommended list.

I am a [Sublime Text Editor](http://www.sublimetext.com/) fan. Before it, I was using [TextMate](http://macromates.com/) a lot but right now I am working in Linux environments too, so I decide to switch to Sublime because is available in all platforms, is not Java, and the plugin ecosystem is pretty atractive.

## Introducing Sublime Package Control

Sublime has a lot of additional features if you install packages, but for being able to do it in a much more comfortable way, the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) is a great approach. And what is that? It is a full-featured package manager that helps you discovering, installing, updating and removing packages.

![Sublime Package Control](http://wbond.net/sublime_packages/img/package_control/command_palette.png)

## Installing the Sublime Package Control

In Sublime, open the console (`Ctrl+`` or `View>Show Console`) and paste the following snippet:

    :::python
    import urllib2,os;
    pf='Package Control.sublime-package';
    ipp=sublime.installed_packages_path();
    os.makedirs(ipp) if not os.path.exists(ipp) else None;
    urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()));
    open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read());
    print 'Please restart Sublime Text to finish installation';

This command creates the Installed Packages folder for you (if necessary), and then downloads the `Package Control.sublime-package` into it.

Now, installing packages is really easy. Package Control is driven by the `Command Pallete`. To open the pallete, press `Ctrl+Shift+P` (Windows, Linux) or `Cmd+Shift+P` (OS X). All Package Control commands begin with `Package Control:`, so start by typing `Package, ` so for installing a new package just type `Package Control:Install Package` and type the name there. That's all!

## Useful packages

### [Djaneiro](https://github.com/squ1b3r/Djaneiro)
Django support.

### [EncodingHelper](https://github.com/SublimeText/EncodingHelper)
Provides the following features:

* Attempts to guess encoding of files.
* Show encoding on status bar.
* Show when the current document is maybe broken because was opened with an incorrect encoding.
* Convert to UTF-8 from a variete of encodings organized in a menu.
* Convert to UTF-8 quickly from guessed encoding via menuitem.
* Convert to UTF-8 automatically when opening a file via some defined encodings found on User preferences.

### [Git](https://github.com/kemayo/sublime-text-2-git/wiki)
Supports status, log viewing, diff viewing, blame, annotate, add files, commit and quick commit.

### [GitHubinator](https://github.com/ehamiter/ST2-GitHubinator)
Allows you to select text in a Sublime Text 2 file, and see the highlighted lines on GitHub's remote repo, if one exists.

### [Pep8Lint](https://github.com/dreadatour/Pep8Lint)
Checks Python files against some of the style conventions in PEP8.

### [PylinterPylinter](https://github.com/biermeester/)
Allows automatic Python source code checking by Pylint. Pylint needs to be installed separately.

### [SublimeAlignment](http://wbond.net/sublime_packages/alignment)
Dead-simple alignment of multi-line selections and multiple selections.  Align multiple selections to the same column by inserting spaces (or tabs) Align all lines in a multi-line selection to the same indent level Align the first = on each line of a multi-line selection to the same column.

### [SublimeCodeIntel](https://github.com/Kronuz/SublimeCodeIntel)
Code intelligence plugin ported from Open Komodo Editor to Sublime Text 2. Supports `PHP, Python, RHTML, JavaScript, Smarty, Mason, Node.js, XBL, Tcl, HTML, HTML5, TemplateToolkit, XUL, Django, Perl, Ruby, Python3`. 

Provides the following features:

* Jump to Symbol Definition.
* Jump to the file and line of the definition of a symbol.
* Imports autocomplete.
* Shows autocomplete with the available modules/symbols in real time.
* Function Call tooltips.
* Displays information in the status bar about the working function.


### [SublimeHtmlTidy](https://github.com/welovewordpress/SublimeHtmlTidy)
Allows you to clean and tidy up your HTML code.

### [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)
Highlights lines of code the linter deems to contain (potential) errors. It also supports highlighting special annotations (for example: TODO) so that they can be quickly located.  Built in linters for the following languages:

* *CoffeeScript* - lint via coffee -s -l.
* *CSS* - lint via built-in csslint.
* *Git Commit Messages* - lint via built-in module based on A Note About Git Commit Messages.
* *Haml* - lint via haml -c.
* *Java* - lint via javac -Xlint.
* *Javascript* - lint via built in jshint, jslint, or the closure linter (gjslint) (if installed).
* *Objective-J* - lint via built-in capp_lint.
* *Perl* - lint via Perl:Critic or syntax+deprecation checking via perl -c.
* *PHP* - syntax checking via php -l.
* *Puppet* - syntax checking via puppet parser validate.
* *Python* - native, moderately-complete lint.
* *Ruby* - syntax checking via ruby -wc.

### [SublimeTODO](https://github.com/robcowie/SublimeTODO)
Extracts and lists TODO comments from open files and project folders.

### [WordHighlight](https://github.com/adzenith/WordHighlight)
Highlights all copies of a word that's currently selected, or, optionally, highlights all copies of a word which currently has the insertion cursor upon it.

## Themes

When installing a new package through the Package Control, there are some special ones named `Themes`. They will change the look and feel of Sublime. Just search them in `Package Control:Install Packages` with the string `Theme - ThemeName`. For activating the theme just open the User Settings Preferences file (Sublime Text 2 -> Preferences -> Settings - User`) and add, append or update the theme entry like this:

    :::python
    {"theme": "Soda Light.sublime-theme" }

###[Soda](https://github.com/buymeasoda/soda-theme/)
Dark and light custom themes.