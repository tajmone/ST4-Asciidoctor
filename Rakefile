=begin "Rakefile" v0.3.1 | 2024/02/15| by Tristano Ajmone
================================================================================
Rake automation for the Sublime Asciidoctor package.
================================================================================
=end

# Custom helpers ...

require './_assets/rake/globals.rb'
require './_assets/rake/asciidoc.rb'

# ==============================================================================
# -------------------------------{  T A S K S  }--------------------------------
# ==============================================================================

task :default => [:guide, :tests_html, :samples]

## Clean & Clobber
##################
require 'rake/clean'
CLOBBER.include(
  'docs/*.html',
  'Examples/*.html',
  'Tests/**/*.html'
)

## Syntax Tests to HTML
#######################

desc "Convert syntax test to HTML"
task :tests_html

# We use the @ precedence modifier so that document-defined
# attributes will always override CLI definitions.

TESTS_ADOC_OPTS = <<~HEREDOC
  --failure-level WARN \
  --verbose \
  --timings \
  --safe-mode unsafe \
  -a experimental@ \
  -a toc@=left \
  -a sectanchors@ \
  -a reproducible@ \
  -a icons@=font \
  -a !caption=@
HEREDOC

FileList['Tests/**/*.asciidoc'].exclude(
    '__*.*',
    '**/_syntax_test_*.*'
  ).each do |f|
  html_doc = f.ext('.html').sub('syntax_test_', '')
  task :tests_html => html_doc
  file html_doc => f do |t|
    AsciidoctorConvert(t.source, html_doc.pathmap("%f"), TESTS_ADOC_OPTS)
  end
end

## AsciiDoc Examples to HTML
############################

desc "Convert examples to HTML"
task :samples

# Here we focus on conversion mode settings only,
# anything else has to be set within the sample docs.

SAMPLES_ADOC_OPTS = <<~HEREDOC
  --failure-level WARN \
  --verbose \
  --timings \
  --safe-mode unsafe
HEREDOC

# We treat any file without '.asciidoc' or '.html' extension
# (except "README.md") as a dependency for all source files,
# since we can't discriminate what depends on what...

SAMPLES_DEPS = FileList['Examples/*.*'].exclude(
  '**/*.asciidoc',
  '**/*.html',
  '**/README.md'
)

FileList['Examples/*.asciidoc'].each do |f|
  html_sample = f.ext('.html')
  task :samples => html_sample
  file html_sample => [f, *SAMPLES_DEPS] do |t|
    AsciidoctorConvert(t.source, html_sample.pathmap("%f"), SAMPLES_ADOC_OPTS)
  end
end

## Build Documentation
######################

desc "Build HTML user guide"
task :guide

GUIDE_SRC = 'docs-src/index.asciidoc'
GUIDE_HTM = 'docs/index.html'

GUIDE_DEPS = FileList[
  GUIDE_SRC,
  'docs-src/*.adoc',
  '_assets/rake/*.rb'
]

GUIDE_ADOC_OPTS = <<~HEREDOC
  -a source-highlighter=rouge \
  -a rouge-style=thankful_eyes \
  --failure-level WARN \
  --verbose \
  --timings \
  --safe-mode unsafe \
  --destination-dir=../docs
HEREDOC

task :guide => GUIDE_HTM

file GUIDE_HTM => GUIDE_DEPS do |f|
  AsciidoctorConvert(GUIDE_SRC, "index.html", GUIDE_ADOC_OPTS)
end
