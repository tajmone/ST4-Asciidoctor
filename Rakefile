=begin "Rakefile" v0.1.0 | 2022/04/16| by Tristano Ajmone
================================================================================
Rake automation for the Sublime Asciidoctor package.
================================================================================
=end

# Custom helpers ...

require './_assets/rake/globals.rb'
require './_assets/rake/asciidoc.rb'

# ==============================================================================
# --------------------{  P R O J E C T   S E T T I N G S  }---------------------
# ==============================================================================

# We use the @ precedence modifier to ensure that document-defined attributes
# will always override CLI definitions.

ADOC_OPTS = <<~HEREDOC
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

# ==============================================================================
# -------------------------------{  T A S K S  }--------------------------------
# ==============================================================================

task :default => :html

## Clean & Clobber
##################
require 'rake/clean'
CLOBBER.include('Tests/**/*.html')

## Syntax Tests to HTML
#######################

desc "Convert syntax test to HTML"
task :html

TEST_DOCS = FileList['Tests/**/*.asciidoc'].exclude('__*.*').each do |f|
  task :default => f.ext('.html')
end

# ==============================================================================
# -------------------------------{  R U L E S  }--------------------------------
# ==============================================================================

rule '.html' => '.asciidoc' do |t|
  AsciidoctorConvert(t.source, ADOC_OPTS)
end
