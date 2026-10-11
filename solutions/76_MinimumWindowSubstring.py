def minWindow(s, t):
    if len(s) < len(t):
        return ""

    tally = {}

    for ch in s:
        if ch in tally:
            tally[ch] += 1
        else:
            tally[ch] = 1

    print(tally)

    tally_dup = tally

    l, r = 0, 0

    while r < len(s):
        

    
    return ""

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
