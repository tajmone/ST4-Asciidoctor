#!/bin/bash
for i in *.asciidoc ; do
  asciidoctor \
    -a toc=left \
    -a reproducible \
    $i
done
