#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def IsSymetric(root1, root2):
    if (root1 == None && root2 == None):
            return True;
    if (root1 == None || root2 == None):
        return False;
    return (root1.val == root2.val) and isMirror(root1.right, root2.left) and isMirror(root1.left, root2.right)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        print(IsSymetric(root,root))

        