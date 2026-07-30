# Aux space complexity = O(1)
# Time Complexity = O(n)
def findDisappearedNumbers(nums):
    missing = []

    for num in nums:
        visit = abs(num) - 1 
        
        if nums[visit] > 0:
            nums[visit] *= -1
    
    print(nums)

    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i+1)

    return missing

# Space Complexity - O (n)
def findDisappearedNumbers_fatty(nums):
    missing = []
    tally = {}

    n = len(nums)

    for i in range(1, n+1):
        tally[i] = 0

    for n in nums:
        tally[n] = 1

    for x in tally.keys():
        if tally[x] == 0:
            missing.append(x)

    return missing 

# Time Complexity - O(n^2) since the 'in' operation is O(n)
def findDisappearedNumbers_slow(nums):
    n = len(nums)

    missing = []

    for i in range(1, n + 1):
        if i not in nums:
            missing.append(i)

    return missing

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))
    