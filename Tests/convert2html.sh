#!/bin/bash

# Delete old HTML files...
find . -name "*.html" -type f -delete

# Convert all from scratch...
for i in *.asciidoc **/*.asciidoc ; do
	asciidoctor \
		-a toc=left \
		-a reproducible \
		-a icons=font \
		-a caption= \
		$i
done
