#! /usr/bin/python

import sys

if len(sys.argv) != 4:
	sys.exit(sys.argv[0] + ": Expecting three command-line arguments: 1st = grade file, 2nd = either 'ByStudent' or 'ByExam', 3rd = exam number (1, 2, or 3 (all exams)---if 'ByStudent' was selected, the 3rd argument should be '3').")

try:
	exam = int(sys.argv[3])
except:
	sys.exit(sys.argv[0] + ": Expecting a positive integer less than or equal to 3.") 

file = open((sys.argv[1]), 'r')
WhatDoYouWant = sys.argv[2]
d = {}

z = 0
for line in file:
	ln = line.split()
	if z != 0 and len(ln) == 5:
		grade_list = [float(ln[3]), float(ln[4]), float(ln[3]) + float(ln[4])]
		d[ln[2]] = grade_list
	z = 1

def calc_average(exam):
	"Calculates the average score for a particulat exam, or over all exams."
	sum = 0.0
	for k, v in d.items():
			sum += v[exam-1]
	avg = sum/len(d)
	if exam == 3:
		avg = avg/2
	return avg

def calc_student_average(student):
	"Calculates the average score for a particular student."
	avg = d[student][2]/2
	return avg
	
if WhatDoYouWant == 'ByExam':
	average = calc_average(exam)
	if exam == 3:
		print "The average score across all exams is", average
	else:
		print "The average score for Exam", exam, "is", average
elif WhatDoYouWant == 'ByStudent':
	if exam == 3:
		for keys in d:
			average = calc_student_average(keys)
			print "The average score of student #", keys, "is:", average
	else:
		sys.exit(sys.argv[0] + ": Your entry for exam is non-sensical.  Try using '3'.")
else:
	sys.exit(sys.argv[0] + ": The second argument must be either 'ByStudent' or 'ByExam' -- no typos are permitted")