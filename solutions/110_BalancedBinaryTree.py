from _TreeNode import *

def isBalanced(root):

    def height(root):
        if not root:
            return 0 

        right_depth = height(root.right)
        if right_depth == -1:
            return -1

        left_depth = height(root.left)
        if left_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1
        
        return 1 + max(left_depth, right_depth)
    
    return height(root) != -1

# Balanced tree → True
t1 = TreeNode(3,
              TreeNode(9),
              TreeNode(20, TreeNode(15), TreeNode(7))
              )
print(isBalanced(t1))  # True

# Unbalanced tree → False
t2 = TreeNode(1,
              TreeNode(2,
                       TreeNode(3, TreeNode(4), TreeNode(4)),
                       TreeNode(3)),
              TreeNode(2)
              )
print(isBalanced(t2))  # False

# # Empty tree → True
# t3 = None
# print(isBalanced(t3))  # True

# # Single node → True
# t4 = TreeNode(1)
# print(isBalanced(t4))  # True

# # One child → True
# t5 = TreeNode(1, None, TreeNode(2))
# print(isBalanced(t5))  # True

# # Chain of three nodes → False
# t6 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
# print(isBalanced(t6))  # False

# # Root's subtrees have equal heights, but are internally unbalanced → False
# t7 = TreeNode(1,
#               TreeNode(2, TreeNode(3, TreeNode(4))),
#               TreeNode(5, None, TreeNode(6, None, TreeNode(7)))
#               )
# print(isBalanced(t7))  # False