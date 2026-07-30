# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
        list_len = 0
        curr = head

        while curr:
            list_len += 1
            curr = curr.next 

        stack = []
        curr = head

        if list_len == 1:
            return True

        for _ in range(list_len//2):
            stack.append(curr.val)
            curr = curr.next

        if list_len % 2 == 1:
            curr = curr.next

        i = 0
        while curr:
            # print(curr.val)
            if curr.val != stack.pop(-1):
                return False   
            curr = curr.next
        return True


def printasList(list1):
     list2 = []
     while list1 != None:
          list2.append(list1.val)
          list1 = list1.next
     print(list2)

print(isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))))
print(isPalindrome(ListNode(1, ListNode(2, None))))

