#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
	sys.exit("Expecting one argument: <num_taxa>")

upper_limit = int(sys.argv[1])

output = open('NumAttachments.txt', 'w')

def calc_num_attach_points(n):
	return 2*n-3

for i in range(3, upper_limit):
	num_attachments = calc_num_attach_points(i)
	output.write(str(i) + " " + str(num_attachments) + "\n")
