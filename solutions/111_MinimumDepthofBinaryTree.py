from _TreeNode import *

def minDepth(root):
    if not root:
        return 0

    if root.right is None:
        return 1 + minDepth(root.left)

    if root.left is None:
        return 1 + minDepth(root.right)

    return 1 + min(minDepth(root.left), minDepth(root.right))
 

t1 = TreeNode(3,
              TreeNode(9),
              TreeNode(20, TreeNode(15), TreeNode(7))
              )
print(minDepth(t1))  # 3

t2 = TreeNode(2, None,
              TreeNode(3, None,
                       TreeNode(4, None,
                                TreeNode(5, None, TreeNode(6))))
              )
print(minDepth(t2))  # 5

