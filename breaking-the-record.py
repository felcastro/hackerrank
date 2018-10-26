def breakingRecords(scores):
	min_broke = 0
	max_broke = 0
	prev_min = scores[0]
	prev_max = scores[0]
	scores = scores[1:]
	for score in scores:
		if score > prev_max:
			prev_max = score
			max_broke += 1
		if score < prev_min:
			prev_min = score
			min_broke += 1
	return (max_broke, min_broke)

print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
