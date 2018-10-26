def climbingLeaderboard(scores, alice):
	scores = sorted(set(scores), reverse = True)
	l = len(scores)
	for a in alice:
		while (l > 0) and (a >= scores[l-1]):
			l -= 1
		print(l+1)

#======================TESTING=========================

x = [100, 100, 50, 40, 40, 20, 10]
y = [5, 25, 50, 120]
print(x)
print(y)
print("  Result: " + str(climbingLeaderboard(x, y)))
print("Expected: " + str([6, 4, 2, 1]))
print("-------------------------------------------------------------")
x = [100, 90, 90, 80, 75, 60]
y = [50, 65, 77, 90, 102]
print(x)
print(y)
print("  Result: " + str(climbingLeaderboard(x, y)))
print("Expected: " + str([6, 5, 4, 2, 1]))
