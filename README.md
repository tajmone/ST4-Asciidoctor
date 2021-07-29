# Asciidoctor Package for SublimeText 3 and 4

Adds [AsciiDoc] support to [SublimeText 3] and 4, targeting [Asciidoctor].

- https://github.com/tajmone/ST3-Asciidoctor

-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3,4" -->

- [About](#about)
    - [Project Status](#project-status)
    - [Goals](#goals)
    - [Issues](#issues)
- [Features](#features)
    - [File Associations](#file-associations)
    - [Syntax Highlighting](#syntax-highlighting)
    - [Keymaps](#keymaps)
    - [Snippets](#snippets)
    - [Symbol Lists](#symbol-lists)
    - [Completions](#completions)
- [Installation](#installation)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)

<!-- /MarkdownTOC -->

-----


# About

This is a SublimeText plug-in (package) that enhances the experience of writing documents using AsciiDoc (AsciiDoctor) markup.
At a high level, this package offers:

- Syntax Highlighting (with customizable color schemes)
- A (growing) library of snippets to save on typing common elements
- A (growing) library of commands that do some "heavy lifting"
- Configuration settings that tell SublimeText how to best work with AsciiDoc (e.g. file associations).


## Project Status

This is a fork of the __[sublimetext-asciidoc]__ package from the [Asciidoctor Project], created by [Matt Neuburg] and [Jakub Jirutka]:

- https://github.com/asciidoctor/sublimetext-asciidoc

The original package is buggy, and that repository has not been maintained (stale since August 2015).
Numerous pull requests with fixes to some of the known problems were never merged.
Furthermore, the original package uses the old `.tmLanguage` syntax format.

This fork addresses all of that.
This is currently considered a "usable alpha" (as of early 2021).
Indeed, it's used daily on large, complicated AsciiDoc projects.
The "alpha" status merely reflects that implementation details are subject to change (e.g. how the syntax scopes are named).

Here's a brief summary of how the original package was improved so far:

- The AsciiDoc syntax was ported from the old `.tmLanguage` syntax format of __Sublime Text 2__ to the `.sublime-syntax` format of __Sublime Text 3__.
(Before migrating, several third party fixes to known problems found in other forks were incorporated. See [Credits section].)
- A suite of syntax tests were added to maintain integrity during development.
- Poorly handled syntax highlighting (for certain markup elements) have either been fixed or disabled.

## Goals

1. *Not settling for a poor syntax-highlighting implementation.* The old (`.tmLanguage`) syntax definition often misinterpreted perfectly valid syntax as being something else. This would cause the highlighting to go wonky part-way through the document.
So markup features that were causing trouble have been disabled here, because "less is more" when having to chose between feature richness and features that actually work.

2. *To reach enough maturity to warrant becoming a full-fledged package hosted on [Package Control].*
Unless and until somebody surprises the AsciiDoc community by releasing an AsciiDoc [language server], this package will have to suffice.

3. *To encourage adoption and feedback,* by providing excellent documentation and responsive support.

4. *To encourage contributions.* Lively discussions are taking place in https://github.com/tajmone/ST3-Asciidoctor/discussions and https://github.com/tajmone/ST3-Asciidoctor/issues.


## Issues

The main problem is that the AsciiDoc syntax is quite complex, so it's not easy to cover (nor predict) every possible combinations of its markup elements, especially so in syntax definitions which are, basically, just huge RegExs-based settings files — ideally, an AsciiDoc package should be implemented as a language server, via [LSP].

Syntax break-downs usually occur due to wrong parsing precedences leading to false positives in various contexts.
Since AsciiDoc offers many alternative ways to express its markup elements, finding the right precedence in every context can be quite hard, especially when introducing new elements in the syntax definition, which often breaks previously defined elements that were working fine.

For the above reasons, it's possible that during the Alpha stage various syntax elements will be temporarily disabled from time to time, due to new contextual problems rising when other elements are added, fixed or reintroduced.


# Features


## File Associations

This package associates AsciiDoc with files that end in: `.ad`, `.adoc`, or `.asciidoc`.


## Syntax Highlighting

This package includes an AsciiDoc-specific syntax definition.
With it, SublimeText will accordingly apply a (customizable) color scheme to any AsciiDoc file.


## Keymaps

| Action             | Default Shortcut                          |   Notes                                   |
|--------------------|-------------------------------------------|-------------------------------------------|
| Auto-Paired        | Asterisks, underscores, backticks, quotation marks | See [KEYMAP_DETAILS.adoc](Docs/KEYMAP_DETAILS.adoc)  |
| Lists and Callouts | <kbd>Enter</kbd>                          | Automatically sets up the next item. See [KEYMAP_DETAILS.adoc](Docs/KEYMAP_DETAILS.adoc)  |
| Comment/Uncomment  | SublimeText's default (usually <kbd>Ctrl</kbd> + <kbd>/</kbd>) | AsciiDoc comments begin with `//` |


## Snippets

|        Name        |                  Trigger                  |   Notes                                   |
|--------------------|-------------------------------------------|-------------------------------------------|
| Button             | `btn` <kbd>Tab</kbd>         | See [SNIPPET_DETAILS.adoc](Docs/SNIPPET_DETAILS.adoc#btn)  |
| Comment Block      | `//` <kbd>Tab</kbd>                       |                                           |
| Document Title     | `h0` <kbd>Tab</kbd>                       |                                           |
| Example Block      |                                           |                                           |
| Footnote Reference | `fnr` <kbd>Tab</kbd>                      |                                           |
| Footnote           | `fn` <kbd>Tab</kbd>                       |                                           |
| Image              | `img` <kbd>Tab</kbd>                      |                                           |
| Keyboard Shortcut  | `kbd` <kbd>Tab</kbd>         | See [SNIPPET_DETAILS.adoc](Docs/SNIPPET_DETAILS.adoc#btn)  |
| Listing Block      | `--` <kbd>Tab</kbd>                       |                                           |
| Passthrough Block  |                                           |                                           |
| Quote Block        | `__` <kbd>Tab</kbd> or `""` <kbd>Tab</kbd> |                                           |
| Section Title 1–5  | `h1` <kbd>Tab</kbd> … `h5` <kbd>Tab</kbd> |                                           |
| Sidebar block      |                                           |                                           |
| Table              | `= `<kbd>Tab</kbd>                        |                                           |


## Symbol Lists

Document and section titles are displayed in the local symbol list ( <kbd>Ctrl</kbd> + <kbd>R</kbd> / <kbd>Cmd</kbd> + <kbd>R</kbd>) and the global symbol list ( <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>).
In the local symbol list, titles are nicely indented.
In the global symbol list, titles will start with `=`, so you will know they belong to AsciiDoc files at a glance. Also they will be on top of the list because of the precedence of `=`.


## Completions

* Provides completions for attributes (built-in and locally defined) and cross references (local anchors and titles).

# Installation

> __IMPORTANT__ — If you have installed the __[sublimetext-asciidoc]__ package, you must uninstall it before attempting to install this package!
>
> If you've installed the __[AsciiDoc][ST2 AsciiDoc]__ package, you're strongly advised to uninstall it, or disable it, or at least to manually associate the AsciiDoc extensions (`.adoc`, `.asciidoc` and `.ad`) with this Asciidoctor plugin.

Right now, this repository is not a full-fledged package that can be installed using the [Package Control] directory.

You should therefore install it manually, via Git:

1. From your terminal, navigate to your Packages subdirectory under the ST3's data directory:
    * OS X: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`
    * Linux: `~/.config/sublime-text-3/Packages/`
    * Windows: `%APPDATA%\Sublime Text 3\Packages\`
2. From that directory, invoke Git to clone this repository into the `Asciidoctor` subdirectory:

        git clone https://github.com/tajmone/ST3-Asciidoctor.git Asciidoctor

3. Restart SublimeText.

> __NOTE__ — The thus installed package won't self update, you'll have to manually run a `git pull` in the package folder, or come up with some automated scripted solution to do so.


# Credits

<!-- MarkdownTOC:excluded -->
## sublimetext-asciidoc

This repository was forked from the __[sublimetext-asciidoc]__ package by the [Asciidoctor Project], created by [Matt Neuburg] and [Jakub Jirutka], released under the MIT License:

```
The MIT License

Copyright 2014 Matt Neuburg <http://www.apeth.net/matt/default.html>
Copyright 2015 Jakub Jirutka <jakub@jirutka.cz> and the Asciidoctor Project.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```


<!-- MarkdownTOC:excluded -->
## asciispec-sublime

Some syntax improvements were also taken from [Brian Thomas Smith]'s own fork of the original repository:

- https://github.com/bsmith-n4/asciispec-sublime


<!-- MarkdownTOC:excluded -->
## AsciiDoc Bundle for TextMate 2

The upstream __[sublimetext-asciidoc]__ package was based on the __[AsciiDoc-TextMate-2.tmbundle]__ by [Matt Neuburg].

<!-- MarkdownTOC:excluded -->
## MarkdownEditing

Most of the commands and keymaps of the upstream __[sublimetext-asciidoc]__ package, as well as some text found in this README document, were based on (or inspired by) the __[MarkdownEditing]__ package by [Brett Terpstra], released under the MIT License:

```
The MIT License (MIT)
Copyright (c) 2012 Brett Terpstra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```


<!-- MarkdownTOC:excluded -->
## Brian Thomas Smith

Before converting from the old `.tmLanguage` format to the newer `.sublime-syntax` format, I've integrated various syntax fixes and improvements from [Brian Thomas Smith]'s __[asciispec-sublime]__ repository (commit [@087a9d00911]), which is also a fork of the __[sublimetext-asciidoc]__ package.

[@087a9d00911]: https://github.com/bsmith-n4/asciispec-sublime/commit/087a9d00911


# Acknowledgments

I'm in debt with the whole [Sublime Forum] community for all their kind support over the years; and I'd like to expressly thank the following users for their support in matters directly related to this project:
[@facelessuser],
[Ashwin Shenoy],
[Keith Hall],
[Raoul Wols].


# Contributing

Any contribution to this project is most welcome, whether it's a suggestion submitted by [opening an Issue], or contributions to its code via pull requests using Git.

All pull requests should be submitted on the `dev` branch, not on `master`.

Furthermore, to preserve a clean history, pull requests will be merged by rebasing on the `dev` branch; so we might ask you to rebase your PR branch again after code reviewing the PR.

Pull requests can contain multiple commits if they address different features and fixes (indeed, one commit per feature is preferable over packing together unrelated fixes and improvements), but multiple commits amending a single feature should be squashed into a single commit before merging.

All pull requests should pass the Travis CI build, which also checks code styles consistency via [EditorConfig], to prevent spurious noise in commits diffs.


# License

This project is licensed under [MIT License].
For the full text of the license, see the [`LICENSE`][LICENSE] file.

```
The MIT License

Copyright 2020 Tristano Ajmone <https://github.com/tajmone>
Copyright 2014 Matt Neuburg <http://www.apeth.net/matt/default.html>
Copyright 2015 Jakub Jirutka <jakub@jirutka.cz> and the Asciidoctor Project.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

<!-----------------------------------------------------------------------------
                               REFERENCE LINKS
------------------------------------------------------------------------------>

[AsciiDoc]: https://asciidoc.org "Visit AsciiDoc website"
[Asciidoctor]: https://asciidoctor.org "Visit Asciidoctor website"
[Install Package Control]: https://packagecontrol.io/installation
[language server]: https://microsoft.github.io/language-server-protocol "Learn more about the Language Server Protocol and language servers"
[LSP]: https://microsoft.github.io/language-server-protocol "Learn more about the Language Server Protocol and language servers"
[MIT License]: http://opensource.org/licenses/MIT/
[opening an Issue]: https://github.com/tajmone/ST3-Asciidoctor/issues/new/choose "Open a new Issue on this repository"
[EditorConfig]: https://editorconfig.org "Visit EditorConfig website"

<!-- XRefs -->

[Credits section]: #credits "Jump to section"

<!-- project files & folders -->

[LICENSE]: ./LICENSE "View license file"

<!-- ST packages -->

[AsciiDoc-TextMate-2.tmbundle]: https://github.com/mattneub/AsciiDoc-TextMate-2.tmbundle "Visit GitHub repository"
[MarkdownEditing]: https://github.com/SublimeText-Markdown/MarkdownEditing "Visit GitHub repository"
[Package Control]: https://packagecontrol.io
[ST2 AsciiDoc]: https://packagecontrol.io/packages/AsciiDoc "View package at PackageControl.io"
[sublimetext-asciidoc]: https://github.com/asciidoctor/sublimetext-asciidoc "Visit GitHub repository"
[asciispec-sublime]: https://github.com/bsmith-n4/asciispec-sublime "Visit GitHub repository"

<!-- ST3 links & docs -->

[SublimeText 3]: https://www.sublimetext.com/3 "Visit Sublime Text website"
[Sublime Forum]: https://forum.sublimetext.com "Visit the Sublime Forum"

[comment markers]: https://docs.sublimetext.io/reference/comments.html#file-format "Learn more on Sublime Text Community Documentation"
[default commands]: https://docs.sublimetext.io/reference/comments.html#related-keyboard-shortcuts "Learn more on Sublime Text Community Documentation"

<!-- people and orgs -->

[@facelessuser]: https://forum.sublimetext.com/u/facelessuser "View @facelessuser's Sublime Forum profile"
[Ashwin Shenoy]: https://forum.sublimetext.com/u/UltraInstinct05 "View Ashwin Shenoy's Sublime Forum profile"
[Brett Terpstra]: https://brettterpstra.com "Visit Brett Terpstra's website"
[Brian Thomas Smith]: https://github.com/bsmith-n4 "View Brian Thomas Smith's GitHub profile"
[Brian Thomas Smith]: https://github.com/bsmith-n4 "View Brian Thomas Smith's GitHub profile"
[Jakub Jirutka]: https://github.com/jirutka "View Jakub Jirutka's GitHub profile"
[Keith Hall]: https://forum.sublimetext.com/u/kingkeith "View Keith Hall's Sublime Forum profile"
[Matt Neuburg]: https://github.com/mattneub "View Matt Neuburg's GitHub profile"
[Raoul Wols]: https://forum.sublimetext.com/u/rwols "View Raoul Wols's Sublime Forum profile"


[Asciidoctor Project]: https://github.com/asciidoctor "View the Asciidoctor Project's profile on GitHub"

<!-- EOF -->

