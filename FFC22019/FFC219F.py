testCases = int(input())
for i in range(testCases):
	[enemies, power] = [int(n) for n in input().split()]
	enemiesStrength = [int(n) for n in input().split()]
	enemiesStrength.sort()
	count = 0
	for p in enemiesStrength:
		if power >= p:
			count += 1
			power -= p
		else:
			break
	print(count) 
