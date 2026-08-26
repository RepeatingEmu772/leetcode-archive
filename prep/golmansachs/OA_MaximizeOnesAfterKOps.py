# Maximize Ones After K Operations
# You are given a binary string s of length n and a non-negative integer k.
# In one operation, you may select an index i such that 0 ≤ i < n − 1 and perform the following update:
# s[i] = max(s[i], s[i + 1])
# The maximum is calculated using the numeric values of the characters. Therefore, s[i] changes from 0 to 1 only when s[i + 1] is 1.
# You may perform at most k operations.
# Return the maximum possible number of 1 characters in s after performing the operations optimally.
# Example 1:
# Input:
# s = "0001"
# k = 2
# Output:
# 3
# Explanation:
# Choose i = 2:
# 0001 → 0011
# Choose i = 1:
# 0011 → 0111
# The resulting string contains three ones.
# Example 2:
# Input:
# s = "01001"
# k = 3
# Output:
# 5
# Explanation:
# 01001 → 01011 → 01111 → 11111
# The resulting string contains five ones.
# Example 3:
# Input:
# s = "1000"
# k = 10
# Output:
# 1
# Explanation:
# The operation only allows a 1 to propagate from right to left. The existing 1 cannot affect any of the zeros to its right.
# Example 4:
# Input:
# s = "0000"
# k = 5
# Output:
# 0
# There is no 1 in the string, so no operation can change a zero into a one.
# Constraints:
# 1 ≤ n ≤ 200,000
# s contains only the characters 0 and 1.
# 0 ≤ k ≤ 1,000,000,000
# Function signature:
# def maximize_ones(s: str, k: int) -> int
# Expected complexity:
# O(n) time and O(1) additional space.