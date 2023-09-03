# Highlighter

Highlighter is a small tool that highlights
leaf level GUI-components in an Android application screenshot by
parsing and processing xml files, thus making it easier for
developers to understand the GUI. 

## Usage
Place the program file in the same folder as the xml files and the corresponding screenshots (in png format). Make sure that the xml files and the png files share the same name. 

Compile and run the program using

```bash
python highlighter.py
```

The program will run on all xml files in the folder. If it encounters an error in an xml file, or cannot find a matching png, that file will be skipped.

Annotated PNG results will be saved to the same folder that the program is in.
