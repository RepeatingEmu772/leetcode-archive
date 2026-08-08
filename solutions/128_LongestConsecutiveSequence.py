def longestConsecutive(nums):
    nums = set(nums)
    longest = 0

    for n in nums:
        if n-1 not in nums:
            n = n + 1
            curr = 0 
            while n in nums:
                curr += 1
                n += 1
        longest = max(longest, curr+1)    
    return longest

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([1,0,1,2]))


