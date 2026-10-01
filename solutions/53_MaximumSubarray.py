# kadane's algo -- bascically does my baggage help me or should i restart?
def maxSubArray(nums):
    max_current = nums[0]
    max_global = nums[0]
    
    for i in range(1,len(nums)):
        max_current = max(nums[i] ,max_current+nums[i])
        max_global = max(max_global, max_current)

    return max_global

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))
