def backspaceCompare(s, t):
    i = j = 0
    skip_i = skip_j = 0

    while i < len(s) and j < len(t):
        if s[i] != "#" and t[j] != "#" and s[i] != t[j]:
            return False
        

    return False

# Time Complexity - O(n)
# Space Complexity - O(n)

def backspaceCompare_heavy(s, t):

    def format(s):
        sf = ""
        
        for sc in s:
            
            if sc == "#":
                sf = sf[:-1]
            else:
                sf += sc

        return sf
    
    return format(s) == format(t)

print(backspaceCompare('ab#c','ad#c'))
print(backspaceCompare('ab##','c#d#'))
print(backspaceCompare('a#c','b'))
