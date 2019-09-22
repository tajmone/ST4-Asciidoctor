#!/bin/bash
for i in *.asciidoc **/*.asciidoc ; do
  asciidoctor \
    -a toc=left \
    -a reproducible \
    -a caption= \
    $i
done
