testCases = int(input())
while testCases:
	testCases -= 1
	[z,n] = [int(elem) for elem in input().split()]
	const = (n * (n-1))/2
	x = 1
	found = False
	while (z - n * x) > 0 and (z - n * x) >= const:
		if ( z - n * x ) % const == 0:
			print("Y",x)
			found = True
			break
		x += 1
	if not found:
		print("N")
