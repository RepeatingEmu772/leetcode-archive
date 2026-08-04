def topKFrequent(nums, k):      
    tally = {}

    for n in nums:
        if n in tally:
            tally[n] += 1

        else:
            tally[n] = 1

    print(tally)

    sorted_items = sorted(tally.items(), key=lambda x: x[1], reverse=True)

    return [num for num, freq in sorted_items[:k]]

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))


