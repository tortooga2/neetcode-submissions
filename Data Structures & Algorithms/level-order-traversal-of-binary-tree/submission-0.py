# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []

        def dfs(root, level):
            if not root:
                return
            
            if not l or len(l) <= level:
                l.append([root.val])
            else:
                l[level].append(root.val)
            
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        return l


        