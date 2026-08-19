# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def printList(head):
    curr = head
    index = 0

    while curr:
        random_val = curr.random.val if curr.random else None

        print(
            f"Node {index}: "
            f"val={curr.val}, "
            f"random={random_val}"
        )

        curr = curr.next
        index += 1


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        curr_new = dummy
        curr_old = head
        directory = {} # {val : node}

        while curr_old:

            curr_new.next = Node(curr_old.val)
            curr_new = curr_new.next            
            directory[curr_old] = curr_new
            curr_old = curr_old.next

        # printList(dummy)
        # print("base copied")

        curr_old = head
        curr_new = dummy.next

        while curr_old:
            if curr_old.random:
                curr_new.random = directory[curr_old.random]

            curr_old = curr_old.next
            curr_new = curr_new.next


        return dummy.next


# Test Case 1
# [[7,null],[13,0],[11,4],[10,2],[1,0]]

n1 = Node(7)
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1.random = None
n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1

head1 = n1

result1 = Solution().copyRandomList(head1)
printList(result1)

# # Test Case 2
# # [[1,1],[2,1]]

# n1 = Node(1)
# n2 = Node(2)

# n1.next = n2

# n1.random = n2
# n2.random = n2

# head2 = n1

# result2 = Solution().copyRandomList(head2)


# # Test Case 3
# # [[3,null],[3,0],[3,null]]

# n1 = Node(3)
# n2 = Node(3)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3

# n1.random = None
# n2.random = n1
# n3.random = None

# head3 = n1

# result3 = Solution().copyRandomList(head3)