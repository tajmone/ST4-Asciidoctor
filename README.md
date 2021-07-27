# Asciidoctor Package for SublimeText 3

Adds [AsciiDoc] support to [SublimeText 3], targeting [Asciidoctor].

- https://github.com/tajmone/ST3-Asciidoctor

-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3,4" -->

- [About](#about)
    - [Project Status](#project-status)
    - [Goals](#goals)
    - [Issues](#issues)
- [Features](#features)
    - [Keymaps](#keymaps)
    - [Snippets](#snippets)
    - [Others](#others)
- [Installation](#installation)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)
- [Contributing](#contributing)
- [License](#license)

<!-- /MarkdownTOC -->

-----


# About

This my personal fork of the __[sublimetext-asciidoc]__ package from the [Asciidoctor Project], created by [Matt Neuburg] and [Jakub Jirutka]:

- https://github.com/asciidoctor/sublimetext-asciidoc

The original package didn't perform too well, frequently breaking up documents highlighting in various common use cases.
The upstream repository has been stale since August 2015, and various third party pull requests with fixes to the known problems were never merged.

Furthermore, the original package uses the old `.tmLanguage` syntax format.


## Project Status

This package is a "usable Alpha".
It's usable since I actually use it every day to work on big sized AsciiDoc projects, but it's still in its Alpha stage since I might arbitrarily change the scopes naming convention at any time.

Here's a brief summary of how the original package was improved so far:

- The AsciiDoc syntax was ported from the old `.tmLanguage` syntax format of __Sublime Text 2__ to the `.sublime-syntax` format of __Sublime Text 3__.
- Before migrating to the `.sublime-syntax` format, I've integrated some third party fixes to know problems, which I found in other forks of the upstream repository (see [Credits section] further break-downs).
- I've added syntax tests to spot broken features and monitor syntax integrity during development.
- I've either fixed or temporarily disabled the markup elements that were breaking up documents.

## Goals

Since I work with AsciiDoc on a daily basis, I need a package that I can rely on, which doesn't break up a document when I use certain markup elements in a same context, or because some special characters are being wrongly parsed as markup formatting.

I was tired of having to resort to horrible hacks to prevent documents break down just because the original syntax was parsing special characters like `*`, `_` or `^` as opening quoting markers, for which there was no closing delimiter, when they were used for other legitimate markup purposes.

So I've opted to temporary disable any markup features which were causing trouble, because "less is more" when you have to chose between feature richness and features that actually work without breaking documents in real usage scenarios.

My main goal is just to have a reliable AsciiDoc syntax which I can use in my daily work; I don't yet know if this project will ever reach maturity and become a full-fledged package hosted on [Package Control].
I keep hoping that one day someone will surprise the AsciiDoc community by releasing an AsciiDoc [language server] — which I believe it's the only viable way to implement a reliable and feature-rich AsciiDoc package.
In the meantime, I'll keep doing my best to improve this package, hoping that third parties might join in and contribute to its growth.

## Issues

The main problem is that the AsciiDoc syntax is quite complex, so it's not easy to cover (nor predict) every possible combinations of its markup elements, especially so in syntax definitions which are, basically, just huge RegExs-based settings files — ideally, an AsciiDoc package should be implemented as a language server, via [LSP].

Syntax break-downs usually occur due to wrong parsing precedences leading to false positives in various contexts.
Since AsciiDoc offers many alternative ways to express its markup elements, finding the right precedence in every context can be quite hard, especially when introducing new elements in the syntax definition, which often breaks previously defined elements that were working fine.

For the above reasons, it's possible that during the Alpha stage various syntax elements will be temporarily disabled from time to time, due to new contextual problems rising when other elements are added, fixed or reintroduced.


# Features

## Keymaps

* Asterisks (strong), underscores (emphasis), backticks (monospaced), English quotation marks, and Czech quotation marks are autopaired and will wrap selected text.
    - If you start an empty pair and hit backspace, both elements are deleted.
    - If you start an empty asterisks pair and hit <kbd>Space</kbd> or <kbd>Tab</kbd>, the right element is deleted (because you probably wanted to start a list, not a strong text).
* At the end of a (un)ordered list item, pressing <kbd>Enter</kbd> will automatically insert the new list item "bullet."
    - Pressing <kbd>Enter</kbd> on the blank list item will remove it.
    - Pressing <kbd>Tab</kbd> on the blank list item, or selected item(s), will increase nesting level and indent it.
    - Pressing <kbd>Shift</kbd> <kbd>Tab</kbd> on the blank list item, or selected item(s), will decrease nesting level and unindent it.
    - You can disable indentation of list items in your settings file.
* At the end of a callouts list item, pressing <kbd>Enter</kbd> will automatically insert the new list item with incremented number.
    - Pressing <kbd>Enter</kbd> on the blank list item will remove it.

## Snippets

|        Name        |                  Trigger                  |
|--------------------|-------------------------------------------|
| Button             | `btn` <kbd>Tab</kbd>                      |
| Comment Block      | `//` <kbd>Tab</kbd>                       |
| Document Title     | `h0` <kbd>Tab</kbd>                       |
| Example Block      |                                           |
| Footnote Reference | `fnr` <kbd>Tab</kbd>                      |
| Footnote           | `fn` <kbd>Tab</kbd>                       |
| Image              | `img` <kbd>Tab</kbd>                      |
| Keyboard Shortcut  | `kbd` <kbd>Tab</kbd>                      |
| Listing Block      | `--` <kbd>Tab</kbd>                       |
| Passthrough Block  |                                           |
| Quote Block        | `__` <kbd>Tab</kbd> or `""` <kbd>Tab</kbd> |
| Section Title 1–5  | `h1` <kbd>Tab</kbd> … `h5` <kbd>Tab</kbd> |
| Sidebar block      |                                           |
| Table              | `= `<kbd>Tab</kbd>                        |
| Anchored Subsection| `[[` <kbd>Tab</kbd>                       |
| Anchor Reference   | `<<` <kbd>Tab</kbd>                       |


(In case you are not familiar, the Button and Keyboard Shortcut snippets are for in-line macros that render the text to resemble UI buttons and keycaps, respectively.)

### Anchored Subsection

This snippet ensures that your anchor names properly conform (lower-case, no spaces).

Type this: `[[` <kbd>Tab</kbd> Navigable Text

And you get this:
```
    [[navigable-text]]
    === Navigable Text
```


### Anchor Reference

Type this: `<<` <kbd>Tab</kbd> Navigable Text

And you get this:
```
    <<navigable-text,Navigable Text>>
```

## Others

* Displays document and section titles in the local symbol list ( <kbd>Ctrl</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>R</kbd>) and the global symbol list ( <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd> / <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>R</kbd>).
    - In the local symbol list, titles are nicely indented.
    - In the global symbol list, titles will start with `=`, so you will know they belong to AsciiDoc files at a glance. Also they will be on top of the list because of the presedence of `=`.
* Defines [comment markers], so you can use [default commands] to comment and uncomment lines of text.
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
[Jakub Jirutka]: https://github.com/jirutka "View Jakub Jirutka's GitHub profile"
[Keith Hall]: https://forum.sublimetext.com/u/kingkeith "View Keith Hall's Sublime Forum profile"
[Matt Neuburg]: https://github.com/mattneub "View Matt Neuburg's GitHub profile"
[Raoul Wols]: https://forum.sublimetext.com/u/rwols "View Raoul Wols's Sublime Forum profile"

[Asciidoctor Project]: https://github.com/asciidoctor "View the Asciidoctor Project's profile on GitHub"

<!-- EOF -->

