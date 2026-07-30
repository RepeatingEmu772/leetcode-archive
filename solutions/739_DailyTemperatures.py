def dailyTemperatures(temperatures):
    wait = [0] * len(temperatures)
    stack = [] # holds pairs [temp, idx]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _, stackI = stack.pop()
            wait[stackI] = i - stackI
        stack.append([t, i])

    return wait

# Time - O(n^2)
def dailyTemperatures_slow(temperatures):
    wait = []
 
    for i in range(len(temperatures)):

        count = 0
        while temperatures[i] >= temperatures[i + count]:
            
            count += 1

            if i + count >= len(temperatures):
                count = 0
                break
        
        wait.append(count)

    return wait


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90 ]))
