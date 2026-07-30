def isPalindrome(s):
    stripped = ""
    
    for c in s:
        if c.isalnum():
            stripped += c.lower()

    # print(stripped)

    for i in range(0, len(stripped)//2):
        if stripped[i] != stripped[len(stripped) -i - 1]:
            # print("Comparing", i,  stripped[i], stripped[len(stripped) - i - 1] )
        
            return False
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
