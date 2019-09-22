# AsciiDoc Syntax Tests

This directory contains the various tests for the AsciiDoc syntax.

-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3" -->

- [Introduction](#introduction)

<!-- /MarkdownTOC -->

-----

# Introduction

Every test file is also a valid AsciiDoc source file, which can be converted via the [`convert2html.sh`][conv.sh] script with the following purposes:

1. Verify with Asciidoctor that the test file is a valid AsciiDoc source, and capture any error.
2. Simplify tracking the syntax tests by reading them as documents, which provide explanations and references links.

The size-bloat added by this approach to the test files shouldn't be a concern, for tests are only carried out by developers and maintainers of the syntax.
On the other hand, this approach simplifies understanding how the test suite works, making it easier to join the project for anyone wishing to contributing to the syntax.

Besides, AsciiDoc being a rather complex syntax, the need for well-documented tests is a felt need, because there are many edge cases to keep in mind during the tests, and because any changes to the syntax definition could easily introduce unexpected breaking behaviours.


<!-----------------------------------------------------------------------------
                               REFERENCE LINKS
------------------------------------------------------------------------------>

[conv.sh]: ./convert2html.sh "View script source"


<!-- EOF -->
