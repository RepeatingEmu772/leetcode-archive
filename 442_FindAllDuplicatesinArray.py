def findDuplicates(nums):
    dups = []

    for num in nums:
        idx = abs(num) - 1

        if nums[idx] < 0:
            dups.append(abs(num))
        else:
            nums[idx] *= -1

    return dups

print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([1,1,2]))
print(findDuplicates([1]))


