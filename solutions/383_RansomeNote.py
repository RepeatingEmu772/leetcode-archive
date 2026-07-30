def canConstruct(ransomNote, magazine):

    for lt in ransomNote:
        if lt not in magazine:
            return False 
        else:
            if ransomNote.count(lt) > magazine.count(lt):
                return False 

def canConstruct(ransomeNote, magazine):
    
    tally = {}

    for c in magazine:
        if c in tally:
            tally[c] += 1
        else:
            tally[c] = 1

    for m in ransomeNote:
        if m not in tally.keys() or tally[m] == 0:
            return False
        else:
            tally[m] -= 1

    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("a", "aab"))
