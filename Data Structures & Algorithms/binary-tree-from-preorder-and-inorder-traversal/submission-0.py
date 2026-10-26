# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indices = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0
            
        

        def build(left, right):
            nonlocal pre_idx

            if left > right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            new_node = TreeNode(val=root_val)
            mid = indices[root_val]
            
            
        
            new_node.left = build(left, mid - 1)
            new_node.right = build(mid + 1, right)

            

            

            return new_node
        
        return build(0, len(preorder)-1)

           
            


            





        