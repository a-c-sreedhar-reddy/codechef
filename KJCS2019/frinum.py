testCases = int(input())
while testCases:
	testCases -= 1
	numbers = int(input())
	numArray = [int(elem) for elem in input().split()]
	if numbers % 2 == 0:
		print(-1)
	else:
		for i in numArray:
			numArray.remove(i)
			if i in numArray:
				numArray.remove(i)
			else:
				print(i) 
