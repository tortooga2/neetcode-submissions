# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        curr_index = 0
        def dfs(node):

            if not node:
                return
            
            nonlocal curr_index
            nonlocal k
            
            dfs(node.left)
            curr_index += 1
            if curr_index == k:
                nonlocal res
                res = node.val
            dfs(node.right)

            

            
            
            

            
        
        dfs(root)
        return res
