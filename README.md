
# Pocket 2 Bookmark Converter

This script converts a Pocket CSV file to a Netscape Bookmark HTML file.

### Background
Due to the service shutdown of getpocket in mid 2025, I had to migrate my Pocket 
link library/bookmarks to another service.

Most of the services only have an import functionality for the Netscape Bookmark 
file format. Contrary to that the exported data from Pocket was a CSV file. In 
addition, the tags exported from Pocket were separated by '|' and not as usual by 
comma.

Due to this, I used the requirement as a short programming excercise and created 
not top-of-the-art Python CLI program, but one that fullfils the requirements and 
a little bit more.

## Features

- Open source
- Cross platform
- Fully pipe-able (use POSIX pipe '|' system for input and output)
- customizable due to command line options 

## Known limitations
- Maybe the error checking could be enhanced
- Even more command line options could be implemented

## Usage/Examples
```
usage: pocket2bookmark_converter.py [-h] [-s [SEPARATOR]] [infile] [outfile]

Convert a Pocket CSV file to a Netscape Bookmark HTML file.

positional arguments:
  infile                Input CSV file
  outfile               Output HTML file

options:
  -h, --help            show this help message and exit
  -s [SEPARATOR], --separator [SEPARATOR]
                        Specify the character used as separator of tags.
```

On the command line for example, it looks like this:
```bash
./pocket2bookmark-converter.py pocket_data.csv bookmark.htm
```


## License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of the GNU General Public License can be found along with this 
program.  If not, see [GNU General Public License v3.0 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html).
