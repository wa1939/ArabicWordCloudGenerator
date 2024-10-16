Arabic Word Cloud Generator

Overview

This script is used to generate a word cloud image from Arabic text contained in an Excel file. It reads data from a specified column, processes the text to remove specific words, and then creates a word cloud with colors inspired by Elm colors. The generated word cloud is saved as a PNG image with a transparent background.

Features

Reads Arabic text from an Excel file.

Customizes the word cloud colors based on specified brand colors.

Supports reshaping and displaying Arabic text properly using arabic_reshaper and bidi.algorithm.

Saves the word cloud with a transparent background.

Requirements

Python Packages

Python 3.x

pandas (data handling)

wordcloud (generating the word cloud)

arabic_reshaper (reshaping Arabic text for correct display)

bidi.algorithm (corrects the visual order of Arabic characters)

To install the required packages, you can use:

pip install pandas wordcloud arabic-reshaper python-bidi openpyxl

Additional Requirements

openpyxl: Required to read the Excel file.

DIN Next LT Arabic Regular.ttf: The font file used to display Arabic characters correctly in the word cloud. Make sure it is placed in the specified path.

Usage

Make sure you have installed all the required packages using the above command.

Update the paths in the script to reflect the correct locations for your files:

Path to the Excel file ('C:/Users/walghamdi/Desktop/Arabiccloude/thesorcefile.xlsx').

Path to the font file ('C:/Users/walghamdi/Desktop/Arabiccloude/DIN Next LT Arabic Regular.ttf').

Path to save the generated image ('C:/Users/walghamdi/Desktop/Arabiccloude/arabic_wordcloud.png').

Run the script to generate the word cloud.

Notes

The words_to_remove list contains common Arabic words that should be filtered out from the word cloud.

You can modify the colors in the color_func function to match your preferred color scheme.

Troubleshooting

If you encounter an error when reading the Excel file, ensure the path is correct and that the file exists.

If the font path is incorrect or the font file is missing, the script may fail to generate the word cloud.

Example

Upon running the script successfully, a word cloud image named arabic_wordcloud.png will be saved in the specified folder.

