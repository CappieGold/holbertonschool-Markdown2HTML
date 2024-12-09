#!/usr/bin/python3
"""
This module provides a script to convert a Markdown file to an HTML file.
"""

import sys
import os

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # If we reach here, no error is raised, just exit with 0
    sys.exit(0)
