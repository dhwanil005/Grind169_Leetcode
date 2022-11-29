# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(rt):
            if rt:
                temp=rt.left
                rt.left=rt.right
                rt.right=temp
                if rt.left:
                    dfs(rt.left)
                if rt.right:
                    dfs(rt.right)
        dfs(root)
        return root