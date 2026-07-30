def lengthofLongestSubstring(s):
    last_seen = {}
    start = 0
    max_len = 0

    for end, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1

        last_seen[ch] = end
        max_len = max(max_len, end - start + 1)

    return max_len

def lengthofLongestSubstring(s):
    start = 0
    end = 0
    max_len = 0

    while end < len(s):
        while s[end] in s[start:end]:
            start += 1

        max_len = max(max_len, end - start + 1)
        end += 1

    return max_len

print(lengthofLongestSubstring("abcabcbb"))
print(lengthofLongestSubstring("bbbbb"))
print(lengthofLongestSubstring("pwwkew"))
print(lengthofLongestSubstring(""))


