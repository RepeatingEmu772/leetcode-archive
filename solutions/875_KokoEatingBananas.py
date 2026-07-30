# import math

def minEatingSped(piles, h):
    lowest_speed = 1
    highest_speed = max(piles)

    while lowest_speed < highest_speed:
        # print(f"lowest: {lowest_speed}, highest: {highest_speed}")
        mid_speed = lowest_speed + ((highest_speed - lowest_speed) // 2)

        time = 0 
        for pile in piles:
            time += pile // mid_speed
            time += 1 if pile % mid_speed != 0 else 0

        # print(f"mid_speed: {mid_speed}, time: {time}\n")
        
        if time <= h:
            highest_speed = mid_speed 

        else:
            lowest_speed = mid_speed + 1

    return lowest_speed

print(minEatingSped([3,6,7,11], 8))
print(minEatingSped([30,11,23,4,20], 6))
print(minEatingSped([30,11,23,4,20], 4))
