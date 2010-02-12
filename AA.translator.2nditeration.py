#!/usr/bin/env python
import sys
AA_file = open('AA.table.txt', 'r')
seq_file = open('sequence.txt', 'r')

AAs = {}
seq = ''
sequence = ''
start_codon = []

#populate the dictionary of codons by amino acids
for line in AA_file:
	ln = line.split()
	AAs[ln[0]] = ln[1]

#convert multi-line sequence to a single string
for line in seq_file:
	line = line.strip()
	seq = seq + line

#verify the sequence is at least one codon long
if len(seq) < 3:
	sys.exit()

def make_sequence(rna, start):
	"Slices the sequence string so it starts with a start codon"
	short_sequence = rna[start:]
	return short_sequence

def translate(short_sequence):
	"Finds a start codon and translates a nucleotide sequence into Amino Acids until a stop codon is encountered."
	y = 0
	protein = ''
	for index, nuc in enumerate(short_sequence):
		if index < len(short_sequence) - 3:
			protein = protein + AAs[short_sequence[index:index + 3]]
			if AAs[short_sequence[index:index + 3]] == 'Stop':
				break
		else:
			break
	return protein

for index, nuc in enumerate(seq):
	if seq[index:index+3] == 'AUG':
		start_codon.append(index)

for item in start_codon:
	sequence = make_sequence(seq, item)
	polyPeptide = translate(sequence)
	print polyPeptide
