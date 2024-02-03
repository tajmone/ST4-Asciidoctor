:::::::::::::::::::::::::::::
:: Asciidoctor_build_docx.bat
:::::::::::::::::::::::::::::
:: Sublime Build script (Windows version) that exports AsciiDoc to DOCX.
::
:: REQUIREMENTS:
::
::   1. This requires that ASCIIDOCTOR is installed on the system path.
::      See https://docs.asciidoctor.org/asciidoctor/latest/install/.
::
::   2. This requires that PANDOC is installed on the system path.
::      See https://pandoc.org/installing.html.
::
::   3. This assumes that there is a default program declared that can
::      open DOCX files (e.g. Libre Office, see:
::      https://www.libreoffice.org/download/download-libreoffice/).
::
:: To invoke this script from inside a *.sublime-build file, use:
::
::     Asciidoctor_build_docx.bat <file_path> <file_base_name> <file_extension>
::
:: where
::     <file_path> is the folder containing the AsciiDoc source file, and

::     <file_base_name> is the root name of the AsciiDoc source file (without
::         the .adoc extension)
::
::     <file_extension> is the extension of the source file (adoc, asciidoc, txt, etc.)
::
:: There are three ways to specify a reference docx file for pandoc to use as a template:
::
::     1. If the AsciiDoc source file contains an attribute definition for
::        :pandoc:, :pandoc-ref:, or :pandoc-reference:, and the value of that
::        attribute exists as a file, then it will be used.
::
::        NOTE: There is nothing special about this being an attribute
::              definition as far as AsciiDoc is concerned. This script
::              searches the source file directly for it. Using attribute
::              syntax just seems appropriate (as opposed to say something
::              buried in a comment). If there are multiple :pandoc...:
::              attributes defined in the file, only the last one will be used.
::              This script will only find :pandoc...: attributes that are in
::              the main source file, not in any included files.
::
::     2. If .\reference.docx exists, it will be used.
::
::     3. If .\.pandoc\reference.docx exists, it will be used.
::
::     4. Otherwise, no reference file will be used.
::

:: The second line of each of these removes any quotes (")
set WORKING_PATH=%1
set WORKING_PATH=%WORKING_PATH:"=%
set BASE_NAME=%2
set BASE_NAME=%BASE_NAME:"=%
set EXTENSION=%3
set EXTENSION=%EXTENSION:"=%

set DATA_DIR=
set DEST_FILE=%BASE_NAME%.docx
set DOCBOOK_FILE=%BASE_NAME%.xml
set SOURCE_FILE=%BASE_NAME%.%EXTENSION%


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::    Step 1: Parse the AsciiDoc file into a DocBook document
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
del /Q /F "%TEMP%\%2.*"
del /Q /F "%WORKING_PATH%\%DEST_FILE%"

call asciidoctor -b docbook -o "%TEMP%\%DOCBOOK_FILE%" "%SOURCE_FILE%"


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::   Step 2: See if there is a Pandoc reference DOCX (template) we can use
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
for /f "tokens=2" %%a in ('findstr /IR ":pandoc[-refnc]*: " "%SOURCE_FILE%"') do set PANDOC_REF_FILE=%%a
if not exist "%PANDOC_REF_FILE%" (
	set PANDOC_REF_FILE="reference.docx"
)
if not exist "%PANDOC_REF_FILE%" (
	set PANDOC_REF_FILE=".pandoc\reference.docx"
)



:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::   Step 3: Use PanDoc to convert it from DocBook to DOCX format
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
if exist "%PANDOC_REF_FILE%" (
	pandoc -f docbook  --reference-doc="%PANDOC_REF_FILE%" -t docx -o %TEMP%\%2.docx "%TEMP%\%DOCBOOK_FILE%"
) else (
	pandoc -f docbook -t docx -o "%TEMP%\%DEST_FILE%" "%TEMP%\%DOCBOOK_FILE%"
)


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::   Step 4: Open the generated DOCX file (using the system-defined default
::           program for .DOCX files)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
if exist "%TEMP%\%2.docx" (
	move /Y "%TEMP%\%DEST_FILE%" "%WORKING_PATH%"
)
if exist "%WORKING_PATH%\%DEST_FILE%" (
	"%WORKING_PATH%\%DEST_FILE%"
)

