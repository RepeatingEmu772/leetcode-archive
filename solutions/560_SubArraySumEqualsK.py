def subarraySum(self, nums: List[int], k: int) -> int:
    prefix_map = {0: 1}
    prefix_sum = 0
    total = 0

    for num in nums:
        prefix_sum += num

        # print(f"num: {num}, prefix_sum: {prefix_sum}") 
        needed = prefix_sum - k
        if needed in prefix_map:
            total += prefix_map[needed]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return total

print(subarraySum([1,1,1], 2))
print(subarraySum([1,2,3], 3))
print(subarraySum([1,2,3,2,1], 3))