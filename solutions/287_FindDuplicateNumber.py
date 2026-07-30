def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

        
    entrance = nums[0]

    while slow != entrance:
        slow = nums[slow]
        entrance = nums[entrance]

    return entrance

        
        

def findDuplicate_slow(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                return nums[i]
    return 0 

print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([3,1,3,4,2]))
print(findDuplicate([3,3,3,3,3]))