# AsciiDoc Samples

This folder contains sample documents to showcase how the syntax and color scheme(s) work.

These samples are for the benefit of package contributors: the contents of this folder are being excluded from the final package by the `export-ignore` rules in the `.gitattributes` settings file.

## Contributors Guidelines

All AsciiDoc files with `.asciidoc` extension inside the folder **MUST BE** valid AsciiDoc documents that will convert with Asciidoctor (Ruby) using the HTML backend and the option `--failure-level WARN` without raising errors nor warnings.

This means that any required external assets (images, code files, and AsciiDoc snippets to be included via `include::` directive) must be present within this folder too. AsciiDoc snippet-files for inclusion should use the `.adoc` file extension, so that Rake will ignore them when building this folder.

The repository `Rakefile` automatically processes this folder: it will convert all `*.asciidoc` documents using the correct settings, so **ALWAYS TEST CONTENTS EDITS TO THIS FOLDER VIA RAKE**.

> **NOTE** — The Rakefile will treat any file with an extension other than `.asciidoc` or `.html` (excluding `README.md`) as if it's a dependency of every `*.asciidoc` file in this folder, so that any changes to these dependencies files will trigger a fresh conversion to HTML of all source document.
>
> Since there's no way to tell which assets belong to which `*.asciidoc` source document (moreover, different documents could be reusing some same assets), this is the easiest and safest approach to automating the build of this folder.

If you wish to include malformed AsciiDoc files — e.g. to show how the syntax can handle malformed or incomplete constructs by gracefully recovering from error, without breaking the whole document — use the `.adoc` extension instead.

If your sample document depends on specific document attributes or AsciiDoc settings, ensure to define them within the document header using attributes (e.g. `:experimental:`, `:icons: font`, ToC settings, etc.).
