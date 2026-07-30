from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

def isAnagram_manual(s, t):
    tally = {}

    for char in s:
        if char in tally:
            tally[char] += 1
        else:
            tally[char] = 1

    for char in t:
        if char in tally:
            tally[char] -= 1
        else:
            return False
    
    for t in tally.keys():
        if tally[t] != 0:
            return False 
        
    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))