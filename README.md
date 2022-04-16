# Asciidoctor Package for Sublime Text 4

Adds [AsciiDoc] support to [Sublime Text 4], targeting [Asciidoctor].

- https://github.com/tajmone/ST3-Asciidoctor

-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3,4" -->

- [About](#about)
    - [Project Status](#project-status)
    - [Goals](#goals)
    - [Challenges](#challenges)
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

This is a Sublime Text package that enhances the experience of writing documents using AsciiDoc (Asciidoctor) markup.

- Syntax Highlighting (with customizable color schemes).
- A (growing) library of snippets to save on typing common elements.
- A (growing) library of commands that do some "heavy lifting".
- Configuration settings that tell Sublime Text how to best work with AsciiDoc (e.g. file associations).


## Project Status

This is a fork of the **[sublimetext-asciidoc]** package from the [Asciidoctor Project], created by [Matt Neuburg] and [Jakub Jirutka]:

- https://github.com/asciidoctor/sublimetext-asciidoc

The original package is buggy, and its repository has not been stale since August 2015.
Numerous pull requests with fixes to some of the known problems were never merged.
Furthermore, the original package uses the old `.tmLanguage` syntax format.

This fork addresses all of that.
This is currently considered a "usable alpha" (as of early 2021).
Indeed, it's used daily on large, complicated AsciiDoc projects.
The "alpha" status merely reflects that implementation details are subject to change (e.g. how the syntax scopes are named).

Here's a brief summary of how the original package was improved so far:

- The AsciiDoc syntax was ported from the old `.tmLanguage` syntax format of **[Sublime Text 2]** to the `.sublime-syntax` format of **[Sublime Text 3]**.
(Before migrating, several third party fixes to known problems found in other forks were incorporated. See [Credits section].)
- A suite of syntax tests were added to maintain integrity during development.
- Poorly handled syntax highlighting (for certain markup elements) have either been fixed or disabled.
- Added `version: 2` key to the syntax definition to enable the new **[Sublime Text 4]** syntax features, like branching, which are going to be very helpful to correctly handle complex syntax constructs and edge cases.

## Goals

1. **Preventing documents breakdown**.
The old (`.tmLanguage`) syntax definition often misinterpreted perfectly valid syntax as being something else, leading to a total breakdown of the document highlighting and all scope-based package features.
So markup features that were causing trouble have been disabled here, because "less is more" when having to chose between feature richness and features that actually work.
2. **Tests Coverage**.
Due to the state of entanglement of the original syntax definition, and to prevent any future changes from breaking existing features, this project strongly focuses on creating a solid syntax testsuite that will be able to detect any breaking changes during work.
3. **Documentation**.
Due to the complexity of the AsciiDoc syntax, all package sources and tests are being well documented in order to allow contributors to easily join the project development and track what features are being covered and what's still missing.
Without descriptive source comments, TODOs annotations and links to reference Asciidoctor documentation it would be hard for contributors to join the project.
4. **Sublime Text 4 Support**.
Enable the latest features of Sublime Text 4, at the cost of dropping backward compatibility with previous versions of the editor.
The new syntax features like contexts branching are powerful additions that should help solve many of the problematic AsciiDoc constructs that were not previously addressable.
5. **Encouraging active participation**.
This fork hopes to gather active participation to the project by other AsciiDoc users via pull requests contributions and using the repository [Discussions] for suggesting future improvements and missing features, and reporting current bugs via [Issues].
6. **Becoming a full-fledged package on [Package Control]**.
Unless and until somebody surprises the AsciiDoc community by releasing an AsciiDoc [language server], this package will keep striving to offer decent support for the AsciiDoc syntax, eventually reaching a stage of maturity that warrants submitting it to the official Package Control channel.

Since the original **[sublimetext-asciidoc]** package went stale in 2015 there have been multiple forks of the original package repository, mostly by individuals (like me) trying to fix and update the syntax in order to be able to use it in their daily work.

It's sad to see that development of the AsciiDoc package for Sublime Text officially hosted and endorsed by the [Asciidoctor Project] ended, leaving behind an unfinished and broken package which is mostly unusable in production.
This, along with the fact that none of the current forks has yet managed to solve all the known problems is an indicator of the challenges posed by the complexity of the AsciiDoc syntax for RegExe-based syntax definitions.

I hope that eventually this fork will manage to break through all these challenges, resulting in a production-usable Sublime Text package for editing AsciiDoc documents.
In the past seven years various people tried to reach this goal, but we're still waiting to see a good AsciiDoc package at [Package Control], so chances are that — realistically speaking — this goal requires cooperative efforts, which is why I've been focusing on documenting the project as best as I could, to make it easier for others to join-in.


## Challenges

The main challenge faced by this package is that the AsciiDoc syntax is quite complex, so it's not easy to cover (nor predict) every possible combinations of its markup elements, especially so in syntax definitions which are, basically, just huge RegExs-based settings files — ideally, an AsciiDoc package should be implemented as a language server, via [LSP], or via a [Tree-sitter] grammar, but unfortunately neither of these standard is officially supported by Sublime Text, although there's a [third party package adding LSP support][sublimelsp].

**[Sublime Text 4]** introduced some new syntax features, like context branching and rewind via `branch` and `fail`, which are going to greatly improve handling complex AsciiDoc constructs and edge cases that were previously hard or impossible to handle.

Syntax break-downs usually occur due to wrong parsing precedence leading to false positives in various contexts.
Since AsciiDoc offers many alternative ways to express its markup elements, finding the right precedence in every context can be quite hard, especially when introducing new elements in the syntax definition, which often breaks previously defined elements that were working fine.

For the above reasons, it's possible that during the Alpha stage various syntax elements will be temporarily disabled from time to time, due to new contextual problems rising when other elements are added, fixed or reintroduced.


# Features

## File Associations

This package associates AsciiDoc with the `.adoc`, `.asc`, and `.asciidoc` file extensions.

## Syntax Highlighting

This package includes an AsciiDoc-specific syntax definition.
With it, Sublime Text will accordingly apply a (customizable) color scheme to any AsciiDoc file.

## Keymaps

|       Action       |                   Default Shortcut                  |                                          Notes                                           |
|--------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------|
| Auto-Paired        | Asterisks, underscores, backticks, quotation marks  | See [KEYMAP_DETAILS.adoc](Docs/KEYMAP_DETAILS.adoc)                                      |
| Lists and Callouts | <kbd>Enter</kbd>                                    | Automatically sets up the next item. See [KEYMAP_DETAILS.adoc](Docs/KEYMAP_DETAILS.adoc) |
| Comment/Uncomment  | ST default (usually <kbd>Ctrl</kbd> + <kbd>/</kbd>) | AsciiDoc comments begin with `//`                                                        |


## Snippets

|        Name        |                  Trigger                   |                           Notes                           |
|--------------------|--------------------------------------------|-----------------------------------------------------------|
| Button             | `btn` <kbd>Tab</kbd>                       | See [SNIPPET_DETAILS.adoc](Docs/SNIPPET_DETAILS.adoc#btn) |
| Comment Block      | `//` <kbd>Tab</kbd>                        |                                                           |
| Document Title     | `h0` <kbd>Tab</kbd>                        |                                                           |
| Example Block      |                                            |                                                           |
| Footnote Reference | `fnr` <kbd>Tab</kbd>                       |                                                           |
| Footnote           | `fn` <kbd>Tab</kbd>                        |                                                           |
| Image              | `img` <kbd>Tab</kbd>                       |                                                           |
| Keyboard Shortcut  | `kbd` <kbd>Tab</kbd>                       | See [SNIPPET_DETAILS.adoc](Docs/SNIPPET_DETAILS.adoc#btn) |
| Listing Block      | `--` <kbd>Tab</kbd>                        |                                                           |
| Passthrough Block  |                                            |                                                           |
| Quote Block        | `__` <kbd>Tab</kbd> or `""` <kbd>Tab</kbd> |                                                           |
| Section Title 1–5  | `h1` <kbd>Tab</kbd> … `h5` <kbd>Tab</kbd>  |                                                           |
| Sidebar block      |                                            |                                                           |
| Table              | `= `<kbd>Tab</kbd>                         |                                                           |


## Symbol Lists

Document and section titles are displayed in the local symbol list ( <kbd>Ctrl</kbd> + <kbd>R</kbd> / <kbd>Cmd</kbd> + <kbd>R</kbd>) and the global symbol list ( <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> / <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>).
In the local symbol list, titles are nicely indented.
In the global symbol list, titles will start with `=`, so you will know they belong to AsciiDoc files at a glance. Also they will be on top of the list because of the precedence of `=`.


## Completions

* Provides completions for attributes (built-in and locally defined) and cross references (local anchors and titles).

# Installation

> **IMPORTANT** — If you have installed the **[sublimetext-asciidoc]** package, you must uninstall it before attempting to install this package!
>
> If you've installed the **[AsciiDoc][ST2 AsciiDoc]** package, you're strongly advised to uninstall it, or disable it, or at least to manually associate the AsciiDoc extensions (`.adoc`, `.asciidoc` and `.asc`) with this Asciidoctor plugin.

Right now, this repository is not a full-fledged package that can be installed using the [Package Control] directory.

You should therefore install it manually, via Git:

1. From your terminal, navigate to your Packages subdirectory under the ST3's data directory:
    * OS X: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`
    * Linux: `~/.config/sublime-text-3/Packages/`
    * Windows: `%APPDATA%\Sublime Text 3\Packages\`
2. From that directory, invoke Git to clone this repository into the `Asciidoctor` subdirectory:

        git clone https://github.com/tajmone/ST3-Asciidoctor.git Asciidoctor

3. Restart Sublime Text.

> **NOTE** — The thus installed package won't self update, you'll have to manually run a `git pull` in the package folder, or come up with some automated scripted solution to do so.


# Credits

<!-- MarkdownTOC:excluded -->
## sublimetext-asciidoc

This repository was forked from the **[sublimetext-asciidoc]** package by the [Asciidoctor Project], created by [Matt Neuburg] and [Jakub Jirutka], released under the MIT License:

```
The MIT License

Copyright 2019-2022 Tristano Ajmone <https://github.com/tajmone>
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

The upstream **[sublimetext-asciidoc]** package was based on the **[AsciiDoc-TextMate-2.tmbundle]** by [Matt Neuburg].

<!-- MarkdownTOC:excluded -->
## MarkdownEditing

Most of the commands and keymaps of the upstream **[sublimetext-asciidoc]** package, as well as some text found in this README document, were based on (or inspired by) the **[MarkdownEditing]** package by [Brett Terpstra], released under the MIT License:

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

Before converting from the old `.tmLanguage` format to the newer `.sublime-syntax` format, I've integrated various syntax fixes and improvements from [Brian Thomas Smith]'s **[asciispec-sublime]** repository (commit [@087a9d00911]), which is also a fork of the **[sublimetext-asciidoc]** package.

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
[Tree-sitter]: https://tree-sitter.github.io "Visit Tree-sitter website"
[sublimelsp]: https://github.com/sublimelsp/LSP/ "Visit the Sublime Text LSP package repository"

<!-- ST3 links & docs -->

[Sublime Text]: https://www.sublimetext.com "Visit Sublime Text website"
[Sublime Text 2]: https://www.sublimetext.com/2 "Visit Sublime Text 2 webpage"
[Sublime Text 3]: https://www.sublimetext.com/3 "Visit Sublime Text 3 webpage"
[Sublime Text 4]: https://www.sublimetext.com "Visit Sublime Text website"
[Sublime Forum]: https://forum.sublimetext.com "Visit the Sublime Forum"

[comment markers]: https://docs.sublimetext.io/reference/comments.html#file-format "Learn more on Sublime Text Community Documentation"
[default commands]: https://docs.sublimetext.io/reference/comments.html#related-keyboard-shortcuts "Learn more on Sublime Text Community Documentation"

<!-- ST packages -->

[AsciiDoc-TextMate-2.tmbundle]: https://github.com/mattneub/AsciiDoc-TextMate-2.tmbundle "Visit GitHub repository"
[MarkdownEditing]: https://github.com/SublimeText-Markdown/MarkdownEditing "Visit GitHub repository"
[Package Control]: https://packagecontrol.io
[ST2 AsciiDoc]: https://packagecontrol.io/packages/AsciiDoc "View package at PackageControl.io"
[sublimetext-asciidoc]: https://github.com/asciidoctor/sublimetext-asciidoc "Visit GitHub repository"
[asciispec-sublime]: https://github.com/bsmith-n4/asciispec-sublime "Visit GitHub repository"

<!-- repo refs -->

[Discussions]: https://github.com/tajmone/ST3-Asciidoctor/discussions "Visit the repository Discussions area"
[Issues]: https://github.com/tajmone/ST3-Asciidoctor/issues "Visit the repository Issues area"

<!-- XRefs -->

[Credits section]: #credits "Jump to section"

<!-- project files & folders -->

[LICENSE]: ./LICENSE "View license file"

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
