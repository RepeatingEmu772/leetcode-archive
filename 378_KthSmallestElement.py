def kthSmallest(matrix, k):
    n = len(matrix)
    
    mod = k % n
    row = k // n

    print(mod, row)
    return matrix[row][mod-1]

# Space - O(n2)
# Time - O (n2logn)
def kthSmallest_fat_slow(matrix, k):
    flatten_list = []

    for row in matrix:
        for val in row:
            flatten_list.append(val)

    flatten_list.sort()
    print(flatten_list)

    return flatten_list[k-1]


print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(kthSmallest([[-5]], 1))


