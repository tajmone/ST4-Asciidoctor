# AsciiDoc Snippets

Snippets collection for the ST4-Asciidoctor package.


-----

**Table of Contents**

<!-- MarkdownTOC autolink="true" bracket="round" autoanchor="false" lowercase="only_ascii" uri_encoding="true" levels="1,2,3" -->

- [Dev Guidelines](#dev-guidelines)
    - [Long Delimiters: 78 Chars](#long-delimiters-78-chars)

<!-- /MarkdownTOC -->

-----

# Dev Guidelines

A few guidelines to enforce consistency across snippets.

## Long Delimiters: 78 Chars

When a snippet emits line-long delimiters these should be 78 characters long.

This applies to all block delimiters which have a variable length, like comment blocks delimiters which consist in four or more slashes (`////`).

Example, the Comment Block snippet will produce the following result:

```asciidoc

//////////////////////////////////////////////////////////////////////////////
text selection
//////////////////////////////////////////////////////////////////////////////

```

where the extra slashes are provided as an ornamental frame-like element for visually enhancing the block from the surrounding context.

The adoption of 78 characters as the standard length for such delimiters is a reasonable arbitrary compromise to prevent line wrapping of the delimiters in the editor (the default wrapping is at 80) as well as ensuring good rendering of the source file in terminals, in side-by-side diffs, and in three-way merging windows for conflict resolutions (e.g. in Sublime Merge).

All snippets that emit such ornamental delimiters should abide to the 78 characters rule, unless there are good reasons for not doing so.

<!-----------------------------------------------------------------------------
                               REFERENCE LINKS
------------------------------------------------------------------------------>



<!-- EOF -->
