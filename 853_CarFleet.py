def carFleet(target, position, speed):
    stack = []

    zipped = zip(position, speed)

    for pos, spd in sorted(zipped)[::-1]:
        # print(f'pos {pos}, spd {spd}') 
        time = (target - pos) / spd
        stack.append(time)
        
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(carFleet(10, [3], [3]))
print(carFleet(100, [0,2,4], [4,2,1]))

 