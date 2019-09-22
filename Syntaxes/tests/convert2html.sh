#!/bin/bash
for i in *.asciidoc ; do
  asciidoctor $i
done
