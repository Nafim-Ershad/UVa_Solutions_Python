a_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 199, 311, 337, 373, 733, 919, 991]	#	Generation of this list would be better
#	Source of list	: https://en.wikipedia.org/wiki/Permutable_prime

while True:
	n = int(input())
	if n==0:
		break
	if n < 10:
		for i in a_primes:
			if i > n:
				if i<10:
					print(i)
				else:	
					#	Because if there is increase in digits, then the number cannot be permutable.
					#	For example, for 7 the next permutable prime number would be 11 which is of a different digit count (2). 7 can be permutable only once where as 11 can be permuted twice.
					print(0)
				break
	elif n <100:
		for i in a_primes:
			if i > n:
				if i<100:
					print(i)
				else:
					#	Same like 7 and 11, taking 97 and 113, they are of different digit count
					print(0)
				break
	else:
		if n>=991:
			print(0)
		else:
			for i in a_primes:
				if i>n:
					print(i) 
					break