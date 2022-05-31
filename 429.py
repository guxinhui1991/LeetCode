# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if root.children : res = [i.val for i in root.children]
        return [root.val] + res


rootTest = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(Solution().levelOrder(rootTest))