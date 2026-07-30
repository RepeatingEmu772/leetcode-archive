# Space Complexity = O(1)
# Time Complexity = O(n) since sum has a complexity of O(n)

# Use arth sum formula: 1 + 2 + ... n = n(n+1)//2
def missingNumber(nums):
    n = len(nums)

    expected = (n * (n + 1)) // 2
    actual = sum(nums)

    return expected - actual


# Space Complexity = O(1)
# Time Complexity = O(nlgn) since sort has a complexity of O(lgn)

def missingNumber_slow(nums):

    n = len(nums)
    nums.sort()

    # print(nums)

    if nums[-1] == n-1: return n

    for i in range((len(nums)-1)):
        # print(i)
        if nums[i + 1] - nums[i] != 1:
            return nums[i] + 1

    return 0

print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
