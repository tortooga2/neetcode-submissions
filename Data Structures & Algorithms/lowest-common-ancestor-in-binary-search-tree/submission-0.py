# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None

        
        def dfs(root):
            nonlocal lca

            if not root:
                return None

            if q.val < root.val and p.val < root.val:
                return dfs(root.left)
            elif q.val > root.val and p.val > root.val:
                return dfs(root.right)
            else:
                return root
        
        return dfs(root)


            
        

        