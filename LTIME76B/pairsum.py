import functools 
testCases = int(input())
while testCases:
	testCases -= 1
	[Alen , queryLen] = [int(elem) for elem in input().split()]
	B = [int(elem) for elem in input().split()]
	while queryLen:
		queryLen -= 1
		[p, q] = [int(elem) for elem in input().split()]
		p, q = p-1, q-1
		if p > q:
			p, q  = q, p
		if (q - p) % 2 == 0:
			print("UNKNOWN")
		else:
			ans = functools.reduce((lambda y, x: x - y), B[p+1:q],B[p])
			print(ans)

