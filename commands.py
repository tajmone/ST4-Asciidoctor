from sublime_plugin import TextCommand
import sublime
import re


class ReplaceFollowingCharacterCommand(TextCommand):
    """ Replace the following character after the cursor with the replacement. """

    def run(self, edit, replacement=' '):
        self.view.run_command('right_delete')
        self.view.run_command('insert', {'characters': replacement})


class AsciidocIndentListItemCommand(TextCommand):
    """ (Un)indent an item or selected items of ordered and unordered list. """

    def run(self, edit, reverse=False):
        view = self.view
        indent_str = self._indent_str()

        # \1: single indentation (optional)
        # \2: remaining indentation followed by markers (except the last one)
        # \3: the last marker
        pattern = re.compile(r'^((?:%s)?)(\s*[*.-]*)([*.-])' % indent_str)

        def indent_line(line_region):
            if line_region.empty(): return ''
            replacement = r'\2' if reverse else indent_str + r'\1\2\3\3'
            return re.sub(pattern, replacement, view.substr(line_region))

        changes = [
            (region, indent_line(region))
            for regions in view.sel()
            for region in view.split_by_newlines(view.line(regions))]

        for item in reversed(changes):
            view.replace(edit, *item)

    def _indent_str(self):
        """ Get indentation string. """
        setting = self.view.settings().get

        if not setting('indent_lists', True):
            return ''
        elif setting('translate_tabs_to_spaces'):
            return setting('tab_size', 2) * ' '
        else:
            return '\t'


class AsciidocExtendCalloutsListCommand(TextCommand):

    def run(self, edit):
        view = self.view

        for selection in view.sel():
            line = view.substr(view.line(selection))
            indent, num = re.findall(r'^(\s*)<(\d+)>', line)[0]
            new_line = "\n%s<%d> " % (indent, int(num) + 1)

            view.insert(edit, selection.begin(), new_line)


class AsciidocRunCommandsCommand(TextCommand):
    """ Run multiple commands in chain. """

    def run(self, edit, commands):
        for command in commands:
            if isinstance(command, str):
                self.view.run_command(command)
            else:
                self.view.run_command(command[0], *command[1:])


class AsciidocRenumberChaptersCommand(TextCommand):
    """ 
    Renumbers all chapter headings. 
    For example, if you have
        ...
        == Chapter Nine: Saving the Cat
        == Chapter Ten: The Mirror Moment
        == Chapter Eleven: Hero Status Achieved
        ...
    and you insert a new chapter between Ten and Eleven (== Chapter X: A Stumbling Block)
    then renumbering will get you:
        ...
        == Chapter Nine: Saving the Cat
        == Chapter Ten: The Mirror Moment
        == Chapter Eleven: A Stumbling Block
        == Chapter Twelve: Hero Status Achieved
        ...
    It also works for all of the following formats:
        == Chapter 9: Saving the Cat
        == Nine: Saving the Cat
        == 9: Saving the Cat
        == Chapter 9
        == Nine
        == 9
    Whatever format it finds, it will replicate.
    """ 
    def run(self, edit):
        self._edit = edit
        self._process_text()

    def _num_to_words(self, num):
        '''Convert an integer between 1-99 into words'''
        units = ['','one','two','three','four','five','six','seven','eight','nine']
        teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
                 'seventeen','eighteen','nineteen']
        tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
                'eighty','ninety']
        words = []
        if num==0: words.append('zero')
        else:
            numStr = '%d'% num 
            numStr = numStr.zfill(2)
            t,u = int(numStr[0]),int(numStr[1])
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
        return ' '.join(words)

    def _get_file_content(self):
        return self.view.substr(sublime.Region(0, self.view.size()))

    def _update_file(self, doc):
        self.view.replace(self._edit, sublime.Region(0, self.view.size()), doc)

    def _process_text(self):
        txt = self._get_file_content()
        lines = txt.splitlines()
        result = []
        chapter_number = 0

        for line in lines:
            m = re.match(r"^== *(Chapter )?([^:]*)(.*)", line, flags=re.IGNORECASE)
            if m:
                chapter_prefix = m.group(1)
                chapter_prefix = chapter_prefix.title() if chapter_prefix else ""
                wrong_number = m.group(2)
                chapter_title = m.group(3)
                chapter_number += 1
                if wrong_number.isdigit():
                    result.append("== {}{}{}".format(chapter_prefix,chapter_number,chapter_title))
                elif re.match(r"^[- a-z]+$", wrong_number, flags=re.IGNORECASE):
                    result.append("== {}{}{}".format(chapter_prefix,self._num_to_words(chapter_number).title(),chapter_title))
                else:
                    result.append(line)
            else:
                result.append(line)

        self._update_file( "\n".join(result))


class AsciidocProseFixupCommand(TextCommand):
    """ 
    Cleans up a manuscript that has been converted to AsciiDoc, e.g. by PanDoc...

    pandoc --from=docx --to=asciidoc --wrap=none --atx-headers --extract-media=extracted-media $FILENAME.docx > $FILENAME..adoc

    """
    def run(self, edit):
        self._edit = edit
        self._process_text()

    def _get_file_content(self):
        return self.view.substr(sublime.Region(0, self.view.size()))

    def _update_file(self, doc):
        self.view.replace(self._edit, sublime.Region(0, self.view.size()), doc)

    def _process_text(self):
        txt = self._get_file_content()

        # Remove any leading spaces
        txt = re.sub(r"^[ \t]+", "", txt)

        # Remove any trailing spaces
        txt = re.sub(r"[ \t]+$", "", txt)

        # Collapse multiple spaces
        txt = re.sub(r"\t", " ", txt)
        txt = re.sub(r"  +", " ", txt)

        # Delete any IDs automatically inserted by PanDoc
        txt = re.sub(r"\[\[_.*]]", "", txt)

        # Shorten table delimiters
        txt = re.sub(r"\|==+", "|===", txt)

        # convert m-dashes to AsciiDoc syntax
        txt = re.sub(r"—", "--", txt)

        # Ensure exactly one space before and after ellipses and m-dashes that are mid-sentence (between words)
        txt = re.sub(r"(\w) *\.\.\.+ *(\w)", "\\1 ... \\2", txt)
        txt = re.sub(r"(\w) *-- *(\w)", "\\1 -- \\2", txt)

        # Make sure all m-dashes are represented by exactly 2 dashes
        txt = re.sub(r" +-+ +", " -- ", txt)

        #Replace figure captions with id and title
        txt = re.sub(r"^Figure (\d+)\s?(.*)", "[[fig-\\1]]\n.\\2\n", txt)

        # Replace references to figures with asciidoc xref
        txt = re.sub(r"Figure (\d+)", "<<fig-\\1>>", txt)

        # Smarten dumb quotes (make them typographic)
        txt = re.sub(r"(^|[^a-z])'(em|do|tis|twas|til)\b", "\\1{rsquo}\\2", txt, flags=re.IGNORECASE)
        txt = re.sub(r"^\"", '"`', txt)
        txt = re.sub(r'^_"', '"`_', txt)
        txt = re.sub(r' "', ' "`', txt)
        txt = re.sub(r'"_(\W*)$', '_`"\\1', txt)
        txt = re.sub(r'"(\W*)$', '`"\\1', txt)
        txt = re.sub(r'"([- .,!?])', '`"\\1', txt)
        txt = re.sub(r'"_([- .,!?])', '_`"\\1', txt)
        txt = re.sub(r"^'", "'`", txt)
        txt = re.sub(r" '", " '`", txt)
        txt = re.sub(r"'\n", "`'", txt)
        txt = re.sub(r"'([- .,!?])", "`'\\1", txt)

        txt = re.sub(r'``"', '`"', txt)
        txt = re.sub(r"``'", "`'", txt)

        # Undo smart quotes, making sure to distinguish a possessive apostrophe from a closing quote
        txt = re.sub(r'“', '"`', txt)
        txt = re.sub(r'”', '`"', txt)
        txt = re.sub(r"‘", "'`", txt)
        txt = re.sub(r"(\w)’(\w)", "\\1'\\2", txt)
        txt = re.sub(r"’", "`'", txt)

        # Ensure bullet point syntax (exactly one space following)
        txt = re.sub(r"^(-+|\*+|\.+) *", "\\1 ", txt)

        # Fix transposed end-of-quotation punctuation -- that is, the punctuation goes inside the quotes
        txt = re.sub(r'`"(,|\.|\?|\!)', "\\1`\"", txt)
        txt = re.sub(r"`'(,|\.|\?|\!)", "\\1`'", txt)

        # Fix misplaced commas near parentheticals 
        txt = re.sub(r",( *\([^)]*?\))", "\\1,", txt)

        # One sentence per line -- allowing for closing quotes and closing italics
        txt = re.sub(r'(\.|\?|\!)(`?["\']?)(_?) +([^a-z])', "\\1\\2\\3\n\\4", txt)

        # Fix false line breaks after abbreviations, single initials and ellipses 
        txt = re.sub(r'(Mrs?|Ms|Drs?|Prof|\baka|\bp|\badj|\bn|\bv|a\.k\.a|e\.g|\bvs|\best|i\.e|P\.O| [A-Z]| \.\.)\. *\n', '\\1. ', txt, flags=re.MULTILINE)

        # HTML Entities to Attributes
        txt = re.sub(r"&apos;", "{rsquo}", txt)
        txt = re.sub(r"&(\w*);", "{\\1}", txt)

        # Scene breaks
        txt = re.sub(r"^ *(#|\*)+ *$", "'''", txt, flags=re.MULTILINE)

        # AsciiDoctor can't handle m-dashes at the end of a quotation.
        txt = re.sub(r' *-- *`"', '{mdash}`"', txt)

        self._update_file(txt)
        