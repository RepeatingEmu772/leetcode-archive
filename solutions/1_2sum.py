def twoSum(nums, target):
    complement = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in complement:
            return [complement[needed], i]
        complement[nums[i]] = i
    
    return []

        


print(twoSum([3,2,4],6))
        