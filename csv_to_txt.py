#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Martina Stüssi & Valentina Vogel
# 14-820-195 & 16-708-919


import csv
import re


with open('happy_moments.csv', newline='') as csvfile, open('happy_moments_def.txt', 'w') as textfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar="")
    for row in spamreader:
        if row:
            if row[0].isdigit():
                try:
                    sentence = re.sub(r'^\s*\"?', "", row[4], flags=re.UNICODE)
                    sentence_clean = re.sub(r'\"?\s*$', "", sentence, flags=re.UNICODE)
                    if len(sentence_clean) < 12:
                        continue
                    #textfile.write((row[4].replace('"', '')))
                    textfile.write(sentence_clean)
                    textfile.write('\n')
                except IndexError:
                    continue
            else:
                continue
        else:
            continue




