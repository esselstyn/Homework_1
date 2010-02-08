#!/usr/bin/env python

max = int(raw_input('Select the maximum value: '))
max = max + 1

#Make a list of all prime numbers between 1 and max
primes = []
for i in range(1, max):
	x = 0
	if i < 4:
		primes.append(i)
	else:
		for j in range(2, i-1):
			if i % j == 0:
				x = 1
		if x == 0:
			primes.append(i)

##reduce the number to primes
for k in range(1, max):
	if k in primes:	##if it is already a prime
		answer = [k]
	else:
		z = 0
		answer = []
		for y in primes:
			if y > 1:
				while z not in primes:
					if k % y == 0:
						z = k / y
						answer.append(y)
						if z in primes:
							answer.append(z)
							break
						else:
							k = z
					else:
						break
	print answer
