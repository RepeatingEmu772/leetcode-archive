def nextGreatestLetter(letters, target):
    low = 0
    high = len(letters) - 1
    ans = letters[0]

    while low <= high:
        mid = low + (high - low) // 2

        if letters[mid] > target:
            ans = letters[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans    
 
print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["c","f","j"], "c"))
print(nextGreatestLetter(["x","x","y","y"], "z"))
