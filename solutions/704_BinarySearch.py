def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid -1

        else:
            return mid
    return -1


def search_o(nums, target):
    return search_recursive(nums, 0, len(nums) - 1, target)

def search_recursive(nums, low, high, target):

    if high < low:
        return -1
    
    middle = low + (high - low) // 2
    
    if target == nums[middle]:
        return middle
    
    elif target < nums[middle]:
        return search_recursive(nums, low, middle - 1, target)

    elif target > nums[middle]:
        return search_recursive(nums, middle + 1, high, target)

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))