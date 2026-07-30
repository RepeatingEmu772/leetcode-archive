def trap(height):
    if len(height) < 3:
        return 0

    left = 0
    trapped = 0

    while left < len(height) - 1:
        right = left + 1
        tallest_right = right

        # Search for a wall at least as tall as the left wall
        while right < len(height) and height[right] < height[left]:
            if height[right] > height[tallest_right]:
                tallest_right = right

            right += 1

        # No wall as tall as the left wall was found
        if right == len(height):
            right = tallest_right

        middle_blocks = sum(height[left + 1:right])

        width = right - left - 1
        water_height = min(height[left], height[right])

        trapped += (width * water_height) - middle_blocks

        left = right

    return trapped

# def trap(height):

#     left = 0
#     right = 1

#     middle_blocks = 0
#     trapped = 0

#     while right < len(height):
#         print(f"trapped: {trapped}, left: {left}, right: {right}, middle_blocks: {middle_blocks}")
#         while height[right] < height[left] and right < len(height) - 1:
#             print(f"right: {right}, left: {left}")
#             middle_blocks += height[right]
#             right += 1
         
#         trapped += ((right - left - 1) * min(height[left], height[right])) - middle_blocks
#         left = right
#         right += 1

#     return trapped

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
