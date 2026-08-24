def minSubArrayLen_old(target, nums):
    min_len = 10**100
    curr_sum = nums[0]

    start = 0
    stop = 1

    if nums[0] >= target:
        return 1 
    
    while stop < len(nums):
        
        curr_sum += nums[stop] 
        
        print(f"start: {start}, Stop: {stop}, curr_sum: {curr_sum}, min_len: {min_len}")

        while curr_sum >= target:
            curr_len = stop - start + 1

            print (f"curr_len: {curr_len}")

            if curr_len < min_len:
                min_len = curr_len
            
            curr_sum -= nums[start]
            start += 1 
            
        
        stop += 1

    while curr_sum >= target:
        curr_sum -= nums[start]
        start -= 1
        min_len -= 1

    return 0 if min_len == 10**100 else min_len

def minSubArrayLen(target, nums):

    min_len = float("inf")
    start = stop = curr_sum = 0

    if nums[0] >= target:
        return 1

    while stop < len(nums):
        # print(f"start: {start}, Stop: {stop}, curr_sum: {curr_sum}, min_len: {min_len}")

        curr_sum += nums[stop]

        while curr_sum >= target:
            # print(f"curr_sum: {curr_sum}, min_len: {min_len}")
            curr_len = stop - start + 1
            min_len = min(curr_len, min_len)

            curr_sum -= nums[start]
            start += 1

        stop += 1

    return 0 if min_len == float("inf") else min_len 


print(minSubArrayLen(4, [1, 4, 4]))
print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(11, [1,2,3,4,5]))


