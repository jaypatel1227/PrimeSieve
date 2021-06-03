# this is script to make a file with all of the prime up to some max number

import math
import numpy as np
import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()



def list_primes(int : max) -> np.array:
	primes = np.arange(2,max+1) # this is intially the list of primes
	num = 2 # start with 2
	# only need to cross out multiples for nums less than sqrt(max)
	while num <= math.ceil(np.sqrt(max)): 
		multiple = num*2 # the first multiple in question
		while (multiple <= max): # until the end of the list
			ind = np.where(primes == multiple) # see if you find the multiple
			if ind[0].size != 0: # now, if you have found the multiple then remove it
				primes[ind[0]] = 0
			multiple += num
		ind = np.array([])
		while num <= max and ind.size == 0:
			num += 1
			ind = np.where(primes == num)[0]
		printProgressBar(num, math.ceil(np.sqrt(max)))
	return primes[np.nonzero(primes)]

def save(int : max):
	f = open('primes_up_to_' + str(max) + '.txt', 'w')
	primes = list_primes(max)
	for prime in primes:
		f.write(str(prime) + '\n')

if __name__ == '__main__':
	max = int(input('Up to what number? '))
	initial = time.perf_counter()
	save(max)
	final = time.perf_counter()
	print('Done in ' + str(final - initial) + ' seconds.')
