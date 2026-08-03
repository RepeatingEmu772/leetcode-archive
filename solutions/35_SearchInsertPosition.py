def searchInsert(nums, target):
    start = 0 
    end = len(nums) - 1

    while start <= end:
        mid = start + ((end - start) // 2)
        # print(f"start: {start}, end: {end}, mid: {mid}")

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
    return start

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))

