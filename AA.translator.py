#!/usr/bin/env python

AA_file = open('AA.table.txt', 'r')
seq_file = open('sequence.txt', 'r')
OutFile = open('AA.output.txt', 'a')

AAs = {}
#dictionaries are one-way maps from keys to values
#orders of keys, values in dicts are unstable
#AAs.iterkeys() iterates over keys
#AAs.itervalues() "	" values
#AAs.iteritems() "	" keys and values

for line in AA_file:
	ln = line.split()
	AAs[ln[0]] = ln[1]

y = 0
for line in seq_file:
	y = y + 1
	seqLab = "seq" + str(y)
	protein = ""
	start = False
	z = 0
	for element in line:
		if start == False:
			if line[z:z+3] == 'AUG':
				protein = AAs['AUG']
				start = True
				x = z + 3
		else:
			if x <= len(line) - 4:
				protein = protein + AAs[line[x:x+3]]
				if AAs[line[x:x+3]] == 'Stop':
					break
			else:
				break
			x = x + 3
		z = z + 1
	if protein != "":
		data = seqLab + "\t" + protein + "\n"
		OutFile.write(data)
	
"""for k, v in AAs.iteritems():
   ....:     if v == 'Arg':
   ....:         print k
CGG
AGG
AGA
CGU
CGC
CGA

In [32]: """
