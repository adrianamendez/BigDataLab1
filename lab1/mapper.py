#!/usr/bin/env python
# mapper.py
import sys

# --- get all lines from stdin ---
for line in sys.stdin:
    # --- remove leading and trailing whitespace---
    line = line.strip()

    if "<TITLE>" in line:
        # --- split the line into words ---
        words = line.split()

        # --- output tuples [word, 1] in tab-delimited format---
        for word in words:
            print('%s\t%s' % (word, "1"))

    if "<PLACES>" in line:
        # --- split the line into words ---
        words = line.split()

        # --- output tuples [word, 1] in tab-delimited format---
        for word in words:
            print('%s\t%s' % (word, "1"))

    if "<TOPICS>" in line:
            # --- split the line into words ---
            words = line.split()

            # --- output tuples [word, 1] in tab-delimited format---
            for word in words:
                print('%s\t%s' % (word, "1"))
