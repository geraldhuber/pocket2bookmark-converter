#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script converts a Pocket CSV file to a Netscape Bookmark HTML file.

For a reference on the specification/structure of the Netscape Bookmark format
use this link:
https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582(v=vs.85)

Copyright (C) 2025 Gerald Huber (GeraldTheDeveloper@mail.de)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__author__ = "Gerald Huber"
__contact__ = "GeraldTheDeveloper@mail.de"
__date__ = "2025-08-21"
__github__ = "https://github.com/geraldhuber"


#### IMPORTS ####
import sys
import csv
import argparse


#### FUNCTIONS ####
def parseAgruments():
    # https://docs.python.org/3.10/library/argparse.html?highlight=argparse#argumentparser-objects
    parser = argparse.ArgumentParser(
        description="Convert a Pocket CSV file to a Netscape Bookmark HTML file.",
        epilog=f"(c) {__date__[:4]} {__author__}",
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True)
    
    # https://docs.python.org/3.10/library/argparse.html?highlight=argparse#nargs
    parser.add_argument('infile', help="Input CSV file", nargs='?', type=str, default=sys.stdin)
    parser.add_argument('outfile', help="Output HTML file", nargs='?', type=str, default=sys.stdout)
    parser.add_argument('-s', '--separator', help="Specify the character used as separator of tags.", nargs='?', type=str, default='|')

    # args = parser.parse_args(["pocket_data.csv", "bookmark.htm"])
    args = parser.parse_args()
    
    # parser.print_help()
    return args

def createOutputHeader(subtitle: str) -> str:
    """Returns the DOCTYPE, META, TITLE etc. html tags as the header of the bookmark file.

    Args:
        subtitle (str): The heading to be displayed in the html file. Usually, the name of the input file.

    Returns:
        str: Returns the html code as a string.
    """
    html_output = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'
    html_output += '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
    html_output += '<TITLE>Bookmarks</TITLE>\n'
    html_output += '<H1>Bookmarks</H1>\n'
    html_output += f'<H2>{subtitle}</H2>\n'
    html_output += '<DL><p>\n'
    return html_output


def convertData(csv_filename: str, file_encoding: str, skip_header: bool=True, input_separator: str='|', output_separator: str=',') -> str:
    """Converts the input file CSV rows to description list terms (DT tags in HTML) elements.

    Args:
        csv_filename (str): the input CSV file
        separator (str): the character used to separate the tags in the input file from each other.
                         The output tag separator is always "," (comma).

    Returns:
        str: Returns the HTML code as a string.
    """

    output_data = ''
    with open(csv_filename, 'r', encoding=file_encoding) as csv_file:
        csv_reader = csv.reader(csv_file, strict=True)
        if skip_header:
            next(csv_reader, None)  # skip the first row / header

        for row in csv_reader:
            title = row[0].strip()
            url = row[1]
            added_date = row[2]
            tags = row[3].replace(input_separator, output_separator)
            output_data += createOutputRow(url, added_date, tags, title)
    return output_data

def createOutputRow(title: str, url: str, added_date: str, tags: str) -> str:
    """Returns with the given parameters a HTML DT-element as a string.

    Args:
        title (str): The title of the bookmarked document.
        url (str): URL of the bookmark
        added_date (str): Date the bookmark was saved.
        tags (str): String of tags, separated by comma, that describe the bookmark.

    Returns:
        str: Returns the HTML DT-element as a string.
    """
    return f'<DT><A HREF="{url}" ADD_DATE="{added_date}" TAGS="{tags}">{title}</A>\n'

def createOutputFooter() -> str:
    """Returns the tailing HTML elements to close open tags as per sepcification.

    Returns:
        str: Returns HTML code as a string.
    """
    return '</DL><p>'


#### MAIN ####
def main():
    args = parseAgruments()

    input_filename = args.infile
    output_filename = args.outfile
    tag_separator = args.separator

    output_html = createOutputHeader(input_filename)
    output_html += convertData(input_filename, 'utf-8', skip_header=True, input_separator=tag_separator)
    output_html += createOutputFooter()

    # Write the html code to the output file
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(output_html)


# Entry point - always one of the last statements
if __name__ == "__main__":
    sys.exit(main())