from _TreeNode import *

def diameterOfBinaryTree(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1

        right = dfs(root.right)
        left = dfs(root.left)

        res[0] = max(res[0], 2 + right + left)

        return 1 + max(right, left)

    dfs(root)
    return res[0]

# Path: 4 → 2 → 1 → 3 (3 edges)
t1 = TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3)
              )
print(diameterOfBinaryTree(t1))  # 3

# Two nodes
t2 = TreeNode(1, TreeNode(2))
print(diameterOfBinaryTree(t2))  # 1

# Single node
t3 = TreeNode(1)
print(diameterOfBinaryTree(t3))  # 0

# Empty tree
t4 = None
print(diameterOfBinaryTree(t4))  # 0

# Chain of five nodes
t5 = TreeNode(1, None,
              TreeNode(2, None,
                       TreeNode(3, None,
                                TreeNode(4, None, TreeNode(5))))
              )
print(diameterOfBinaryTree(t5))  # 4

# Balanced tree: longest path crosses the root
t6 = TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3, TreeNode(6), TreeNode(7))
              )
print(diameterOfBinaryTree(t6))  # 4

# Longest path does NOT pass through the root
# Path: 6 → 4 → 3 → 2 → 5 → 7 → 8 (6 edges)
t7 = TreeNode(1,
              TreeNode(2,
                       TreeNode(3, TreeNode(4, TreeNode(6))),
                       TreeNode(5, None, TreeNode(7, None, TreeNode(8)))),
              None
              )
print(diameterOfBinaryTree(t7))  # 6