def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2 
    full = len(A) + len(B)
    half = full // 2

    if len(nums1) > len(nums2):
        A, B = nums2, nums1
    # print(A, B)

    l, r = 0, len(A) - 1 

    while True:
        m = l + (r - l) // 2
        # print(l, m , r)

        i = m # middle of smaller array
        j = half - (i + 1) - 1

        A_left = A[i] if i >= 0 else float("-inf")
        A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
        B_left = B[j] if j >= 0 else float("-inf")
        B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

        if A_left > B_right:
            r = i - 1 

        elif B_left > A_right:
            l = i + 1

        else:
            # odd or even 
            if full % 2:
                return min(A_right, B_right) / 1
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2


print(findMedianSortedArrays([1,2,3,4,5,6,7,8], [1,2,3,4, 5]))
print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
