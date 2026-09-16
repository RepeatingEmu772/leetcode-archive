def numRescueBoats(people, limit):
    people.sort()
    
    boats = 0
    left, right = 0, len(people) - 1

    while left <= right:

        if left < right and people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1
    

    return boats

# print(numRescueBoats([1,2], 3))
print(numRescueBoats([3,2,2,1], 3))
print(numRescueBoats([3,5,3,4], 5))
