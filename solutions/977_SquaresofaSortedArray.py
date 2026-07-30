def sortedSquares(nums):
    p1 = 0
    p2 = len(nums) - 1

    res = []

    while p1 <= p2:
        
        print(f"p1: {p1} p2: {p2}")

        if abs(nums[p1]) > abs(nums[p2]):
            res.append(nums[p1]*nums[p1])
            p1 += 1
        
        elif abs(nums[p1]) < abs(nums[p2]):
            res.append(nums[p2]*nums[p2])
            p2 -= 1

        else:
            res.append(nums[p2]*nums[p2])
            p2 -= 1
    
    return res[::-1]
    

def sortedSquares_trivial(nums):
    
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    nums.sort() 
    return nums


print(sortedSquares([-10000,-9999,-7,-5,0,0,10000]))
print(sortedSquares([-7,-3,2,3,11]))


