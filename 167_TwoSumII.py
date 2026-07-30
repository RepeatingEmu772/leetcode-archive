def twoSum(numbers, target): 
    i = 0
    j = len(numbers) - 1 

    while i < j:
        curr_sum = numbers[i] + numbers[j]

        if curr_sum == target:
            return [i+1, j+1]
        
        elif curr_sum > target:
            j -= 1

        elif curr_sum < target:
            i += 1

    return []


print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))



