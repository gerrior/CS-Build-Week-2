# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        result = []

        self.innerInorderTraversal(root, result)

        return result

    def innerInorderTraversal(self, root, result):
        if root != None:
            self.innerInorderTraversal(root.left, result)
            result.append(root.val)
            self.innerInorderTraversal(root.right, result)

a = Solution()

b = TreeNode(1, None, None)
b.right = TreeNode(2, None, None)
b.right.left = TreeNode(3, None, None)

print(a.inorderTraversal(b))
