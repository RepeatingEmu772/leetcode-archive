class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printasList(list1):
     list2 = []
     while list1 != None:
          list2.append(list1.val)
          list1 = list1.next
     print(list2)
