#!/usr/bin/env python

#Reduce function for checking coordinates column PREM_TYP_DESC

import sys
import string


current_key = None
current_count = 0
key = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    #print(line.split('\t',1))
    key, count = line.split('\t',1)

    try:
        count = int(count)
        key = key.strip()
    except ValueError:
        continue
        
        
    if current_key == key:
        current_count += count
    else:
        if current_key:
            # write result to STDOUT
            print '%s,%s' % (current_key, current_count)
        current_count = count
        current_key = key

print '%s,%s' % (current_key, current_count)
