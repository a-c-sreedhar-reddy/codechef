import functools
testCases = int(input())
while testCases:
	testCases -= 1
	[students,queries] = [int(elem) for elem in input().split()]
	studentsSizes = [int(elem) for elem in input().split()]
	sizedict = {}
	for ssize in studentsSizes:
		if ssize not in sizedict:
			sizedict[ssize] = 1
		else:
			sizedict[ssize] += 1
	appended = []
	summ = 0
	valuesList = list(sizedict.values())
	valuesList.sort(reverse = True)
	for sizeCoun in valuesList:
		appended.append(summ + sizeCoun)
		summ += sizeCoun
	while queries:
		queries -= 1
		query = int(input())
		if query > len(appended):
			print(appended[-1])
		else:
			print(appended[query-1])

