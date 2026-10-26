# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, largest_value):
            if not node:
                return
            
            if node.val >= largest_value:
                nonlocal res
                res += 1
            
            largest_value = max(largest_value, node.val)
            
            
            dfs(node.left, largest_value)
            dfs(node.right, largest_value)
        
        dfs(root, root.val)
        return res
