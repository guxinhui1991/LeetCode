# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

if __name__ == '__main__':
    arr = [4,2,7,1,3,6,9]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(root)
    print()
    Solution().invertTree(root)
    inOrder(root)