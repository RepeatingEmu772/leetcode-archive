def largestRectangleArea(heights):
    stack = []
    max_width = 0
    
    for i, height in enumerate(heights):
        curr_max_width = max(max_width, height)

        while stack and curr_max_width > max_width:
            curr_max_width = max(min(stack.pop(),), )

    return 0

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,4]))

