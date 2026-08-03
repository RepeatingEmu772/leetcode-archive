def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + ((end - start) // 2)
        print(f"start: {start}, end: {end}, mid: {mid}")


        if nums[mid] == target: return mid 

        # check if LEFT is sorted 
        if nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1

            else:
                start = mid + 1 

        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1 

            else:
                end = mid - 1


    return -1

print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))

