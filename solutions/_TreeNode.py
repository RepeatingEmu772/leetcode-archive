from typing import Optional
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def tree_to_array(root: Optional[TreeNode]) -> list[Optional[int]]:
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Remove unnecessary trailing nulls
    while result and result[-1] is None:
        result.pop()

    return result


def print_tree(root: Optional[TreeNode]) -> None:
    print(tree_to_array(root))