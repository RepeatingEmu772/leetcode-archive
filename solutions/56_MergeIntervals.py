def merge(intervals):
    intervals.sort()

    merged = []

    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    return merged


def merge_o(intervals):
    intervals.sort()

    merged = []
    curr = 0

    while curr < len(intervals):
        print(merged)
        if merged:
            last_start, last_end = merged[-1]

            if last_end >= intervals[curr][0]:
                merged.pop()
                merged.append([last_start, max(last_end, intervals[curr][1])])
            else:
                merged.append(intervals[curr])
        else:
            merged.append(intervals[curr])
        curr += 1
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[4,7],[1,4]]))
print(merge([[1,4], [2,3]]))

