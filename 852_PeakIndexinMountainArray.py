def peakIndexInMountainArray(arr):
    low = 0
    high = len(arr) - 1 

    while high > low:
        mid = low + ((high - low) // 2)

        if arr[mid] < arr[mid + 1]:
            low = mid + 1 

        else:
            high = mid

    return low


print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))
 

