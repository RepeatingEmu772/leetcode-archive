def largestRectangleArea(heights):
    stack = [] #monotonic stack -> (i, height)
    max_area = heights[0]

    for i, h in enumerate(heights):
        # print(f"{stack}")
        start = i 

        while stack and stack[-1][1] > h:
            prev_i, prev_h = stack.pop()
            max_area = max(prev_h * (i - prev_i), max_area)
            start = prev_i
            
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,4])) 
print(largestRectangleArea([2]))
print(largestRectangleArea([2, 4, 5, 3]))


