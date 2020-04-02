#!/usr/bin/env python3
"""Usage: grep.py PATTERN FILE [FILE...]
Print lines from each FILE matching regular expression PATTERN. Pass `-` for
standard input.
"""

import sys
import fileinput as fi
import logging as log
import re

# modul logging umožňuje rozčlenit zprávy uživateli do různých úrovní
# důležitosti. v pořadí od nejméně důležité to jsou DEBUG, INFO, WARNING, ERROR
# a CRITICAL. defaultně se zobrazují jen zprávy s důležitostí WARNING a vyšší;
# pokud chceme jít níž, musíme si to nakonfigurovat:
log.basicConfig(level=log.INFO)


def grep(pattern, lines):
    """Print lines matching pattern."""
    for line in lines:
        if re.search(pattern, line):
            print(line, end="")


def parse_argv(argv):
    """Parse script arguments."""
    # pokud dostaneme míň než dva parametry, ručně vyvoláme ValueError
    if len(argv) < 2:
        raise ValueError
    # jinak bereme první parametr jako pattern a veškeré zbývající jako cesty k
    # souborům na prohledání
    pattern, paths = argv[0], argv[1:]
    return pattern, paths


def main(argv):
    """Main entry point of script."""
    try:
        pattern, paths = parse_argv(argv)
    except ValueError:
        log.critical(__doc__.strip())
        sys.exit(1)
    log.info(f"Searching for {pattern!r} in {paths!r}.")
    try:
        grep(pattern, fi.input(paths))
    except FileNotFoundError as err:
        log.critical(__doc__.strip())
        log.critical(err)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])