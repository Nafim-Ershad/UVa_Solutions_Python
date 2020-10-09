def sieve():
	seve = list(range(1000001))
	seve[0] = seve[1] = 0
	for i in range(1000001):
		if seve[i]>0:
			for j in range(i*i, 1000001, i):
				seve[j]=0
	return seve


s = sieve()
t = int(input())
ans = ""
for _ in range(t):
	primes = []; d = {}
	L, U = map(int, input().split())
	for i in range(L, U+1):
		if s[i]:
			primes+=[s[i]]
	n = len(primes)
	for i in range(1, n):
		k = str(primes[i]-primes[i-1])
		if k not in d:
			d[k] = 1
		else:
			d[k] += 1
	m = max(d.values()) if d.values() else 0
	p = 0
	for i, j in d.items():
		if j==m and m!=0:
			p+=1; g=i
			if p>1:
				break	# optimized to 2s
	if p==1:
		print("The jumping champion is {}".format(g))
	else:
		print("No jumping champion")