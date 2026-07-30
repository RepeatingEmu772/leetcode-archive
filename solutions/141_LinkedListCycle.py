class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   

# Constant memory -- 2 pointers
def hasCycle(head):
    if not head or not head.next:
        return False
    
    fast = slow = head

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


def hasCycle2(head):
    if not head or not head.next:
        return False
    
    seen = []

    while head:
        print(seen)
        
        if head in seen:
            return True
        
        seen.append(head)
        head = head.next
    
    return False

list1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4, None)))) #not the case
list2 = ListNode()

print(hasCycle(list1))
print(hasCycle(list2))
