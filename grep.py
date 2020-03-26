#!/usr/bin/env python3
#program env vyhledá preferovanou verzi programu, přes který se skript spustí (lokace pomocí "which env")
# příkaz chmod +x grep.py

import sys
import regex as re


pattern, path = sys.argv[1:]
with open(path) as file:
    for line in file:
        line = line.strip("\n")
        if re.search(pattern, line):
            print(line)