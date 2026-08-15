from _LinkedList import *

def mergeKLists_slow(lists):
    dummy = ListNode()
    curr = dummy

    while any(lists):
        min_val = float("inf")
        min_node = None
        min_idx = -1

        for i, l in enumerate(lists):
            if l and l.val < min_val:
                    min_node = l
                    min_val = l.val
                    min_idx = i

        curr.next = min_node
        curr = curr.next
        lists[min_idx] = lists[min_idx].next
        
    return dummy.next

def mergeKLists(lists):
    def mergeTwoLists(list1, list2):
        dummyhead = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        else:
            dummy.next = list2

        return dummyhead.next

    if not lists:
        return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            list1 = lists[i]

            if i + 1 < len(lists):
                list2 = lists[i + 1]
            else:
                list2 = None

            mergedLists.append(mergeTwoLists(list1, list2))

        lists = mergedLists

    return lists[0]


l1 = ListNode(1, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, ListNode(6))

printasList(mergeKLists([l1, l2, l3]))
printasList(mergeKLists([]))
printasList(mergeKLists([ListNode()]))
