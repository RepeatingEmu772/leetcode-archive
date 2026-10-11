def CombinationSum(candidates, target):


def CombinationSum_slow(candidates, target):
    combinations = []

    def backtrack(curr_candidates):
        print("checking cands: ", curr_candidates)
        if sum(curr_candidates) > target:
            return

        if sum(curr_candidates) == target:
            combinations.append(curr_candidates.copy())
            return
        
        for n in candidates:
            curr_candidates.append(n)
            backtrack(curr_candidates)
            curr_candidates.pop()

    backtrack([])
    unique_comb = []
    
    for comb in combinations:
        comb.sort()
        if comb not in unique_comb:
            unique_comb.append(comb)

    return unique_comb


print(CombinationSum([2,3,6,7], 7))
# print(CombinationSum([2,3,5], 8))
# print(CombinationSum([2], 1))
