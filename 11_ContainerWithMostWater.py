def maxArea(height):
    max_trapped = 0 

    i = 0
    j = len(height) - 1

    while i < j:
        can_trap = min(height[i], height[j]) * (j - i)
        max_trapped = max(max_trapped, can_trap)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_trapped

def maxArea_slow(height):
    max_trapped = -1

    for i in range(len(height) - 1):
        it = i + 1 
        
        while it < len(height):

            # print(f"h: {min(height[i], height[it])}, w: {(it - i)} ")
            can_trap = min(height[i], height[it]) * (it - i)
            max_trapped = max(max_trapped, can_trap)
            it += 1

    return max_trapped


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))

