# Moores voting Aglo
def majorityElement(nums):
    count = candidate = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count += 1
        
        else: # elif candidate != num:
            count -= 1

    return candidate

# time complexity = O(n)
# space complexity = O(n)
def majorityElement_fat(nums):
    tally = {}

    for num in nums:
        if num in tally:
            tally[num] += 1
        else:
            tally[num] = 1

    majority = len(nums) // 2 + 1

    for i in tally.keys():
        if tally[i] >= majority:
            return i

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
