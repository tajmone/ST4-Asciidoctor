#!/bin/bash
for i in *.asciidoc **/*.asciidoc ; do
  asciidoctor \
    -a toc=left \
    -a reproducible \
    -a icons=font \
    -a caption= \
    $i
done
