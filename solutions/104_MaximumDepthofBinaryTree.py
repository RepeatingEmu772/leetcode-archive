from _TreeNode import *

def maxDepth(root):
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)


t1 = TreeNode(  3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7))
                )
print(maxDepth(t1))

t2 = TreeNode(1, None, TreeNode(2))
print(maxDepth(t2))


