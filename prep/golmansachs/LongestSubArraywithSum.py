# Longest Subarray With Sum ≤ K
# You are given an array nums containing positive integers and a positive integer k.
# Return the length of the longest contiguous subarray whose sum is less than or equal to k.
# Example 1
# Input:
# nums = [1, 2, 1, 4, 1]
# k = 5

# Output:
# 3
# Explanation: The longest valid subarray is [1, 2, 1]. Its sum is 4, which is at most 5.
# Example 2
# Input:
# nums = [3, 1, 2, 1, 1]
# k = 4

# Output:
# 3
# Explanation: The longest valid subarray is [1, 2, 1], whose sum is 4.
# Example 3
# Input:
# nums = [6, 7, 8]
# k = 5

# Output:
# 0
# No non-empty subarray has a sum at most 5.
# Example 4
# Input:
# nums = [1, 1, 1, 1]
# k = 10

# Output:
# 4
# The entire array has a sum at most 10.
# Constraints
# 1 ≤ nums.length ≤ 100,000
# 1 ≤ nums[i] ≤ 10,000
# 1 ≤ k ≤ 1,000,000,000
# Function signature
# def longest_subarray(nums: list[int], k: int) -> int:
# Target complexity:
# Time:  O(n)
# Space: O(1)

def longest_subarray(nums: list[int], k: int) -> int:
    # Sliding window approach
    max_len = float("-inf")
    start = stop = curr_sum = 0

    while stop < len(nums):
        print(f"start: {start}, Stop: {stop}, curr_sum: {curr_sum}, max_len: {max_len}")

        curr_sum += nums[stop]

        while curr_sum > k:
            curr_sum -= nums[start]
            start += 1
            
        curr_len = stop - start + 1
        max_len = max(curr_len, max_len)
        stop += 1

    return 0 if max_len == float("-inf") else max_len


print(longest_subarray([1, 2, 1, 4, 1], 5))
print(longest_subarray([3, 1, 2, 1, 1], 4))
print(longest_subarray([6, 7, 8], 5))