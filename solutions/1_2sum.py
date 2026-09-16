def twoSum(nums, target):
    needed = {}

    for i in range(len(nums)):
        # print(needed)
        # need = 
        # print(need)
        if nums[i] in needed:
            return [i, needed[nums[i]]]

        needed[target - nums[i]] = i

    return []

def twoSum_o(nums, target):
    complement = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in complement:
            return [complement[needed], i]
        complement[nums[i]] = i
    
    return []

        


print(twoSum([3,2,4],6))
        