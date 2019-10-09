# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:    
        # return TreeBuilderRecursive.buildTree(preorder, inorder)
        return TreeBuilderIterative.buildTree(preorder, inorder)

    
class TreeBuilder:
    @staticmethod
    def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
        pass
    

"""
pre     [3,9,20,15,7]
in .    [9,3,15,20,7]

         3
        / \
      9     20
            / \
          15  7
          
          
PreIDX =  7
parent = None
Stack =  [     ]
"""
# Time O(n), Space O(n)
class TreeBuilderIterative(TreeBuilder):

    @staticmethod
    def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        
        #Map to look up position in inorder array
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:            
            node = TreeNode(val)
            if idx_map[node.val] < idx_map[stack[-1].val]:
                stack[-1].left = node
            else:
                parent = None
                while stack and idx_map[node.val] > idx_map[stack[-1].val]:
                    parent = stack.pop()
                parent.right=node
            stack.append(node)
        return root
        
        
class TreeBuilderRecursive(TreeBuilder):
    preorder = None
    inorder = None
    idx_map = None
    root_idx = None
        
    @staticmethod
    def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:    
        TreeBuilderRecursive.preorder = preorder
        TreeBuilderRecursive.inorder = inorder
        TreeBuilderRecursive.idx_map = {val:idx for idx, val in enumerate(inorder)}
        TreeBuilderRecursive.root_idx = 0
        
        return TreeBuilderRecursive.buildTreeHelper(0, len(inorder))
    
    @staticmethod    
    def buildTreeHelper(left_start, right_end ):
        # If there is no subtree to compute
        if left_start == right_end: 
            return None;
        
        node_val = TreeBuilderRecursive.preorder[TreeBuilderRecursive.root_idx]
        node = TreeNode(node_val)
        
        split_idx = TreeBuilderRecursive.idx_map[node_val]
        
        TreeBuilderRecursive.root_idx = TreeBuilderRecursive.root_idx + 1
        
        node.left = TreeBuilderRecursive.buildTreeHelper(left_start, split_idx)
        node.right = TreeBuilderRecursive.buildTreeHelper(split_idx+1, right_end)
        return node       
        
        
        