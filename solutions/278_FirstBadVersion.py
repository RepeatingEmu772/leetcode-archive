def isBadVersion(n):
     if n > 1:
          return True
     else:
          return False

def firstBadVersion(n):
    if n == 1:
            return n if isBadVersion(n) else 0

    def firstBadVersionRecur(low, high):
        cur = low + (high - low) // 2
        print(cur)

        if isBadVersion(cur) and not isBadVersion(cur-1):
            return cur
        
        elif isBadVersion(cur):
            return firstBadVersionRecur(0, cur-1)
        
        else:
            return firstBadVersionRecur(cur+1, high)
        
    return firstBadVersionRecur(0, n+1)
        
print(firstBadVersion(2))