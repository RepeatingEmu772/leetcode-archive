def pivotIndex(nums):
    prefix_sum = 0
    postfix_sum = sum(nums)

    for i in range(len(nums)):
        postfix_sum -= nums[i]

        if prefix_sum == postfix_sum:
            return i
        else:
            prefix_sum += nums[i]    

    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))


