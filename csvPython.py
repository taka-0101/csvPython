# -*- coding: utf-8 -*-

import sys
import struct
import csv

f = open('C:/Users/fics/Desktop/data.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

csvlist = []
csvlist.append(str(0))
print(csvlist)

writer.writerow(csvlist)

f.close()