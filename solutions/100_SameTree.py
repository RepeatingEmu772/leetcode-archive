from _TreeNode import *

def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)



# Identical trees → True
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p1, q1))  # True

# Same values, different structure → False
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))
print(isSameTree(p2, q2))  # False

# Same structure, different values → False
p3 = TreeNode(1, TreeNode(2), TreeNode(3))
q3 = TreeNode(1, TreeNode(2), TreeNode(4))
print(isSameTree(p3, q3))  # False

# Both empty → True
p4 = None
q4 = None
print(isSameTree(p4, q4))  # True

# Only one tree is empty → False
p5 = None
q5 = TreeNode(1)
print(isSameTree(p5, q5))  # False

# Identical single nodes → True
p6 = TreeNode(1)
q6 = TreeNode(1)
print(isSameTree(p6, q6))  # True

# Extra node deeper in one tree → False
p7 = TreeNode(1,
              TreeNode(2, TreeNode(4), None),
              TreeNode(3)
              )
q7 = TreeNode(1,
              TreeNode(2),
              TreeNode(3)
              )
print(isSameTree(p7, q7))  # False

# Identical larger trees → True
p8 = TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3, None, TreeNode(6))
              )
q8 = TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3, None, TreeNode(6))
              )
print(isSameTree(p8, q8))  # True