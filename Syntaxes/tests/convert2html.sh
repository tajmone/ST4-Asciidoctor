#!/bin/bash
for i in *.asciidoc ; do
  asciidoctor -a toc=left $i
done
