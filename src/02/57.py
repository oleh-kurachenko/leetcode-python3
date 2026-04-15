from typing import Optional, List
from leetcode.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.paths: List[str] = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        assert root

        self.binary_tree_path_step(root, [])
        return self.paths

    def binary_tree_path_step(self, root: TreeNode, path: List):
        path.append(root.val)

        if not root.left and not root.right:
            self.paths.append("->".join(str(v) for v in path))

        if root.left:
            self.binary_tree_path_step(root.left, path)
        if root.right:
            self.binary_tree_path_step(root.right, path)

        path.pop()
