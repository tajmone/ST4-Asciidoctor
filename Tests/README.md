# AsciiDoc Syntax Test Suite

This directory contains the test suite for the AsciiDoc ST3 syntax.


-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3" -->

- [Directory Contents](#directory-contents)
- [Introduction](#introduction)
- [Running the Tests](#running-the-tests)
- [Adding Test Files](#adding-test-files)
- [Disabled Tests](#disabled-tests)

<!-- /MarkdownTOC -->

-----

# Directory Contents

- [`/blocks/`][blocks/] — block elements.
- [`/quotes/`][quotes/] — inline quote markup elements.
- `./syntax_test_*.ascidoc` — tests for markup elements without a category.
- `_syntax_test_*.ascidoc` — disabled test files that fail the test.
- [`convert2html.sh/`][conv.sh] — convert test files to HTML.

Test files are grouped in subfolders according to category; tests which don't belong to any specific category are kept in the the root directory.

`___*.*` — Files and folders with a name beginning with three underscores will be ignored by Git.


# Introduction

Every test file is also a valid AsciiDoc source file, which can be converted via the [`convert2html.sh`][conv.sh] script with the following purposes:

1. Verify with Asciidoctor that the test file is a valid AsciiDoc source, and capture any formatting errors and edge cases (i.e. formatting not working as expected).
2. Simplify tracking the syntax tests by reading them as documents that explain the nature of the tests, providing examples and and references links.

The size-bloat added by this approach to the test files shouldn't be a concern, for tests are only carried out by developers and maintainers of the syntax.
On the other hand, this approach simplifies understanding how the test suite works, making it easier to join the project for anyone wishing to contributing to the syntax.

Besides, AsciiDoc being a rather complex syntax, the need for well-documented tests is a felt need, because there are many edge cases to keep in mind during the tests, and because any changes to the syntax definition could easily introduce unexpected breaking behaviors.


# Running the Tests

To run the tests:

1. Open and select the `Syntaxes/Asciidoctor.sublime-syntax` file in ST3,
2. Hold <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> to bring up the __Build With__ options,
3. Select __Syntax Tests__.

After having run the tests once, you can henceforth use just <kbd>Ctrl</kbd>+<kbd>B</kbd> to run further tests.

Alternatively, you can use the menus __Tools__ » __Build With__ and __Tools__ » __Build__.

For more info on how syntax testing works, see:

- [Sublime Text 3 Documentation » Syntax Definitions » Testing]


# Adding Test Files

Every test file must be named according to the `syntax_test_<markup element>.ascidoc` convention, and the very first line must contain the following comment:

```asciidoc
// SYNTAX TEST "Packages/Asciidoctor/Syntaxes/Asciidoctor.sublime-syntax"
```

# Disabled Tests

All tests must pass without any error in the package published on `master` branch; therefore, any failing test file must be renamed by prefixing an underscore (`_syntax_test_*.ascidoc`), thus excluding it from ST3 tests.

There can be various reasons why a test file is disabled:

- It catches some edge case problems that need to be addressed.
- Its target markup element was temporarily disabled in the syntax.

Whatever the reason, we keep them in the repository so that they can be quickly re-enabled by removing the leading `_` from their name, and resume working on the markup elements they target.


<!-----------------------------------------------------------------------------
                               REFERENCE LINKS
------------------------------------------------------------------------------>

[Sublime Text 3 Documentation » Syntax Definitions » Testing]: https://www.sublimetext.com/docs/3/syntax.html#testing "Read official ST3 docs on testing syntaxes"


<!-- files & folders -->

[blocks/]: ./blocks "Navigate to folder"
[quotes/]: ./quotes "Navigate to folder"

[conv.sh]: ./convert2html.sh "View script source"

<!-- EOF -->
