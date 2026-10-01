def Jump(nums):
    steps = 0
    l = r = 0

    while r < len(nums) - 1:
        fatherest = 0
        for i in range(l, r + 1):
            fatherest = max(i + nums[i], fatherest)

        l = r + 1
        r = fatherest
        steps += 1

    return steps 

print(Jump([2,3,1,1,4]))