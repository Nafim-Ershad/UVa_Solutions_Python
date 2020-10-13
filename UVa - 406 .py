def sieve_eres():	# Creates a sieve of eresthonsis
	sieve = list(range(1001))
	for i in range(2, 1001):
		if sieve[i]:
			for j in range(i*i, 1001, i):
				sieve[j] = 0
	return set(sieve[1:])


sieve = sieve_eres()

n, c = map(int, input().split())
primes = []; size = 0
for i in range(1, n+1):
	if i in sieve:
		primes += [i]
		size += 1	# Size pf the list of primes within the range

if size&1:
	p = (2*c)-1
else:
	p = 2*c

if p>=size:
	print(str(n) + ' ' + str(c) + ': ' + " ".join(map(str, primes)) + "\n")
else:
	i = 0; j = size
	while size>p:
		i+=1; j-=1
		size-=2
	print(str(n) + ' ' + str(c) + ': ' + " ".join(map(str, primes[i:j])) + "\n")	# As middle of the prime list is to be taken
