def threeSum(nums):
    nums.sort()
    res = []

    for k in range(len(nums)):
        if k > 0 and nums[k] == nums[k - 1]:
            continue

        target = -nums[k]
        i = k + 1
        j = len(nums) - 1

        while i < j:
            curr_sum = nums[i] + nums[j]

            if curr_sum == target:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1

                while i < j and nums[i] == nums[i - 1]:
                    i += 1

                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

            elif curr_sum < target:
                i += 1
            else:
                j -= 1

    return res


print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0]))
