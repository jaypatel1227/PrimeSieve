# this is script to make a file with all of the prime up to some max number

import math
import numpy as np
import time

def list_primes(int : max) -> np.array:
	primes = np.array(range(2,max+1)) # this is intially the list of primes
	num = 2 # start with 2
	# only need to cross out multiples for nums less than sqrt(max)
	while num <= math.ceil(np.sqrt(max)): 
		multiple = num*2 # the first multiple in question
		while (multiple <= max): # until the end of the list
			ind = np.searchsorted(primes, multiple) 
			# binary search to find where multiple would be if it was in the list
			# now, if you have found the multiple then remove it
			if ind < primes.size and primes[ind] == multiple:
				primes = np.delete(primes, ind)  
			multiple += num
		ind = np.searchsorted(primes, num) # find the next present number in the list 
		num = primes[ind+1] if ind <= primes.size else max
	return primes

def save(int : max):
	f = open('primes_up_to_' + str(max) + '.txt', 'w')
	primes = list_primes(max)
	for prime in primes:
		f.write(str(prime) + '\n')

if __name__ == '__main__':
	max = int(input())
	initial = time.perf_counter()
	save(max)
	final = time.perf_counter()
	print('Done in ' + str(final - initial) + ' seconds.')
