import heapq

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for n in nums[k:]:
        print(heap)
        if n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)

    return heap[0]

def findKthLargest_sort(nums, k):
    nums.sort()
    return nums[-k]

def findKthLargest_On2(nums, k):
    # curr_max = -1

    for _ in range(k-1):
        nums.remove(max(nums)) 
    
    return max(nums)


print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
