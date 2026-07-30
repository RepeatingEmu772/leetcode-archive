def findMin(nums):
    left = 0
    right = len(nums) - 1

    # i = 0 

    while left < right:
        # i += 1
        # print(f"left: {left} right: {right}")
        mid = left + ((right - left) // 2)

        # print(f"mid: {mid}")

        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            right = mid

    return nums[left]

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))
print(findMin([1]))
print(findMin([1, 2]))

