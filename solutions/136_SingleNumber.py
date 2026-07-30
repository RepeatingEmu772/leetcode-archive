# Space Complexity - O(1)
# Time Complexity - O(n)
def singleNumber(nums):
    missing = 0
    for num in nums:
        missing ^= num
    return missing

# Space Complexity - O(n)
# Time Complexity - O(n)
def singleNumber_fatty(nums):
    tally = {}

    for num in nums:
        if num in tally:
            tally[num] += 1
        else:
            tally[num] = 1

    for tal in tally:
        if tally[tal] == 1:
            return tal
         
    return -1

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))
