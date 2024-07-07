# Python code
class TrieNode:
    def __init__(self):
        self.childNode = [None for _ in range(26)]

        self.isLeaf = False
        # This will keep track of number of strings that are
        # stored in the Trie from root node to any Trie node.
        self.wordCount = 0

##############################################################################################################
#
#
# 1. Insertion in Trie Data Structure:
#
#
##############################################################################################################

def insert_key(root, key):
    # Initialize the currentNode pointer
    # with the root node
    currentNode = root

    # Iterate across the length of the string
    for c in key:
        # Check if the node exist for the current
        # character in the Trie.
        if currentNode.childNode[ord(c) - ord('a')] == None:
            # If node for current character does not exist
            # then make a new node
            newNode = TrieNode()

            # Keep the reference for the newly created
            # node.
            currentNode.childNode[ord(c) - ord('a')] = newNode

        # Now, move the current node pointer to the newly
        # created node.
        currentNode = currentNode.childNode[ord(c) - ord('a')]

    # Increment the wordEndCount for the last currentNode
    # pointer this implies that there is a string ending at
    # currentNode.
    currentNode.wordCount += 1
    currentNode.isLeaf = False


def countChildNode(s):
    if s.isLeaf: return 0
    count_Arr = [0 if i==None else 1 for i in s.childNode]
    return sum(count_Arr)

def firstValidChildNode(s):
    for i, val in enumerate(s):
        if val is not None:
            return i
    return -1

def commonPrefix(arr, n, root):
    for i in range(n):
        insert_key(root, arr[i])

    res = ''
    max_count = 1
    for i in range(len(root.childNode)):
        if root.childNode[i]:
            count = 1
            cur_pre = chr(97+i)
            s = root.childNode[i]
            while not s.isLeaf and countChildNode(s)<=1:
                count += 1
                idx = firstValidChildNode(s.childNode)
                cur_pre+= chr(97+idx)
                s = s.childNode[idx]

            if count>max_count: res = cur_pre

    return res



# Driver code to test the code
n = 4
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
root = TrieNode()
print(commonPrefix(arr,n, root))