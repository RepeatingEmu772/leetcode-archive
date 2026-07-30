def groupAnagram(strs):
    grouped = []
    seen = {}
    group_idx = 0


    for st in strs:
        sorted_st = ''.join(sorted(st))

        if sorted_st in seen:
            grouped[seen[sorted_st]].append(st)

        else:
            # add to seen along with indx
            seen[sorted_st] = group_idx
            grouped.append([st])
            group_idx += 1
        

    return grouped

print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagram([""]))
print(groupAnagram(["a"]))

 