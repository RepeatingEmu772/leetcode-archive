def subsets(nums):
    res = []
    curr = []

    def backtrack(i):
        if i >= len(nums):
            res.append(curr.copy())
            return

        # include
        curr.append(nums[i])
        backtrack(i + 1)

        # not include
        curr.pop()
        backtrack(i + 1)

    backtrack(0)
    return res


print(subsets([1,2,3]))
print(subsets([0]))
