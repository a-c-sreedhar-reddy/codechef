testCases = int(input())
while testCases:
	testCases -= 1
	scoreTimes = int(input())
	knowsScore = False
	ourScore, otherScore = 0, 0
	while scoreTimes:
		scoreTimes -= 1
		[scoreType, score1, score2] = [int(elem) for elem in input().split()]
		if scoreType == 1:
			knowsScore = True
			ourScore = score1
			otherScore = score2
		if scoreType == 2:
			if score1 == score2:
				knowsScore = True
				ourScore = score1
				otherScore = score2
			elif knowsScore and (score1 < ourScore or score2 < otherScore):
				knowsScore = True
				ourScore = score2
				otherScore = score1	
			elif knowsScore and (score2 < ourScore or score1 < otherScore):
				knowsScore = True
				ourScore = score1
				otherScore = score2
			else:
				knowsScore = False

		if knowsScore:
			print("YES")
		else:
			print("NO")
