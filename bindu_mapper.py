#!/usr/bin/env python
import sys
import re
#input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    count = 0
    # increase counters
    try:
        for word in words[-5:]:
            count = count + 1
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #tab-delimited; the trivial word count is 1
            if len(word)>0 and not word.isdigit() and word!="" and word != "VEHICLE TYPE CODE 1" and word != "VEHICLE TYPE CODE 2" and word != "VEHICLE TYPE CODE 3" and word != "VEHICLE TYPE CODE 4" and word != "VEHICLE TYPE CODE 5" and not re.search('\.', word):
                    print word + '    1'
    except Exception:
        continue

