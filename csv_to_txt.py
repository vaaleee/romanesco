#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Valentina Vogel
# 16-708-919

import sys
import csv

with open('happy_moments.csv', newline='') as csvfile, open('happy_moments.txt', 'w') as textfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row:
            if row[0].isdigit():
                try:
                    textfile.write((row[3].replace('"', '')))
                    textfile.write('\n')
                except IndexError:
                    continue
            else:
                continue
        else:
            continue

