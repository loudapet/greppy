#!/usr/bin/env python3
# docstring = dokumentační řetězec; složí se do kouzelné proměnné __doc__
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""
#program env vyhledá preferovanou verzi programu, přes který se skript spustí (lokace pomocí "which env")
# příkaz chmod +x grep.py
import sys
import regex as re

try:
    pattern, path = sys.argv[1:]
except ValueError:
    print(__doc__.strip(), file=sys.stderr)
    sys.exit(1)
try:
    with open(path) as file:
        for line in file:
            line = line.strip("\n")
            if re.search(pattern, line):
                print(line)
except FileNotFoundError as err:
    print(__doc__.strip(), file=sys.stderr)
    print(err, file=sys.stderr)
    sys.exit(1) #úspěch nenastal, normální je 0