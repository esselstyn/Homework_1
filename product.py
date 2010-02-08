#!/usr/bin/env python

input = open('NumAttachments.txt', 'r')

product = 1

for line in input:
	data = line.split()
	product  = product * int(data[1])
	print data[0],
	print product
