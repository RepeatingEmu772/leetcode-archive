def charReplacement(s, k):
    freq_map = [0] * 26
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        print("curr_window", s[left:right+1])
        print(freq_map)
        freq_map[ord(ch) - ord('A')] += 1
        max_freq = max(freq_map)

        print("r", right, "l", left, "ma", max_freq)
        while (right - left + 1) - max_freq > k:
            freq_map[ord(s[left]) - ord('A')] -= 1
            left += 1
            max_freq = max(freq_map)

        max_len = max(right - left + 1, max_len)
            
    return max_len

print(charReplacement("ABAB", 0))
# print(charReplacement("AABABBA", 1))
