#!/usr/bin/env python3
# docstring = dokumentační řetězec; složí se do kouzelné proměnné __doc__
"""Usage: grep.py PATTERN FILE

Print lines from FILE matching regular expression PATTERN.

"""
#program env vyhledá preferovanou verzi programu, přes který se skript spustí (lokace pomocí "which env")
# příkaz chmod +x grep.py
import sys
import regex as re

def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        line = line.strip()
        if re.search(pattern, line):
            print(line)
            
def parse_argv(argv):
    pattern,path = argv[1:]
    return pattern, path

def main():
    try:
        pattern, path = parse_argv(sys.argv)
    except ValueError:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)
        
    try:
        with open(path) as file:
            grep(pattern, file)
    except FileNotFoundError as err:
        print(__doc__.strip(), file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1) #úspěch nenastal, normální je 0

if __name__ == "__main__":
    main(sys.argv[1:])