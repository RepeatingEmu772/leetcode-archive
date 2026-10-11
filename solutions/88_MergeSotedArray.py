def merge(nums1, nums2, m, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 > -1 and p2 > -1:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1

def merge_cheeky(nums1, nums2, m, n):
    nums1[m:] = nums2

    nums1.sort()
    return nums1


print(merge([1,2,3,0,0,0], [2,5,6], 3, 3))