def mergeOverlappingIntervals(intervals):
    # Write your code here.
	intervals = sorted(intervals, key=lambda x: x[0])
	final = []
	for i, interval in enumerate(intervals):
		if not final:
			final.append(interval)
		else:
			prev = final[-1]
			if prev[1] >= interval[0]:
				final.pop()
				final.append([prev[0], max(prev[1], interval[1])])
			else:
				final.append(interval)
		
    return final