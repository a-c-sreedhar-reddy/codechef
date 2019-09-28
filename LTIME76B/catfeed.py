def isCurrentRoundValid(currentRound):
    return len(currentRound) == len(set(currentRound))
testcases = int(input())
while testcases:
    testcases -= 1
    [cats, cans]  = [int(elem) for elem in input().split()]
    order = [int(elem) for elem in input().split()]
    valid = True
    while len(order) and valid:
        currentround = order[:cats]
        del order[:cats]
        valid = isCurrentRoundValid(currentround)
    if valid:
        print("YES")
    else:
        print("NO")



