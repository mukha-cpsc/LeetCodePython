class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        Solution.inorderTraversal(Solution(), root.left)

        print (root.value)

        Solution.inorderTraversal(Solution(), root.right)

t1 = TreeNode(1)
t1.left = TreeNode(2)
