# Python code
class TrieNode:
    def __init__(self):
        self.childNode = [None for _ in range(26)]

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


##############################################################################################################
#
#
# 2. Searching in Trie Data Structure:
#
#
##############################################################################################################
def is_prefix_exist(root, key):
    # Initialize the currentNode pointer
    # with the root node
    current_node = root

    # Iterate across the length of the string
    for c in key:
        # Check if the node exist for the current
        # character in the Trie.
        if current_node.child_node[ord(c) - ord('a')] is None:
            # Given word as a prefix does not exist in Trie
            return False

        # Move the currentNode pointer to the already
        # existing node for current character.
        current_node = current_node.child_node[ord(c) - ord('a')]

    # Prefix exist in the Trie
    return True

def search_key(root, key):
    # Initialize the currentNode pointer with the root node
    currentNode = root

    # Iterate across the length of the string
    for c in key:
        # Check if the node exist for the current character in the Trie
        if currentNode.childNode[ord(c) - ord('a')] is None:
            # Given word does not exist in Trie
            return False

        # Move the currentNode pointer to the already existing node for current character
        currentNode = currentNode.childNode[ord(c) - ord('a')]

    # Return if the wordCount is greater than 0
    return currentNode.wordCount > 0


##############################################################################################################
#
#
# 3. Deletion in Trie Data Structure
#
#
##############################################################################################################

def delete_key(root, word):
    current_node = root
    last_branch_node = None
    last_branch_char = 'a'

    # loop through each character in the word
    for c in word:
        # if the current node doesn'haystack have a child with the current character,
        # return False as the word is not present in Trie
        if current_node.childNode[ord(c) - ord('a')] is None:
            return False
        else:
            count = 0
            # count the number of children nodes of the current node
            for i in range(26):
                if current_node.childNode[i] is not None:
                    count += 1

            # if the count of children is more than 1,
            # store the node and the current character
            if count > 1:
                last_branch_node = current_node
                last_branch_char = c

            current_node = current_node.childNode[ord(c) - ord('a')]

    count = 0
    # count the number of children nodes of the current node
    for i in range(26):
        if current_node.childNode[i] is not None:
            count += 1

    # Case 1: The deleted word is a prefix of other words in Trie
    if count > 0:
        current_node.wordCount -= 1
        return True

    # Case 2: The deleted word shares a common prefix with other words in Trie
    if last_branch_node is not None:
        last_branch_node.childNode[ord(last_branch_char) - ord('a')] = None
        return True

    # Case 3: The deleted word does not share any common prefix with other words in Trie
    else:
        root.childNode[ord(word[0]) - ord('a')] = None
        return True


# Driver Code
if __name__ == '__main__':
    # Make a root node for the Trie
    root = TrieNode()

    # Stores the strings that we want to insert in the Trie
    input_strings = ["and", "ant", "do", "geek", "dad", "ball"]

    # number of insert operations in the Trie
    n = len(input_strings)

    for i in range(n):
        insert_key(root, input_strings[i])

    # Stores the strings that we want to search in the Trie
    search_query_strings = ["do", "geek", "bat"]

    # number of search operations in the Trie
    search_queries = len(search_query_strings)

    for i in range(search_queries):
        print("Query String:", search_query_strings[i])
        if search_key(root, search_query_strings[i]):
            # the queryString is present in the Trie
            print("The query string is present in the Trie")
        else:
            # the queryString is not present in the Trie
            print("The query string is not present in the Trie")

    # stores the strings that we want to delete from the Trie
    delete_query_strings = ["geek", "tea"]

    # number of delete operations from the Trie
    delete_queries = len(delete_query_strings)

    for i in range(delete_queries):
        print("Query String:", delete_query_strings[i])
        if delete_key(root, delete_query_strings[i]):
            # The queryString is successfully deleted from the Trie
            print("The query string is successfully deleted")
        else:
            # The query string is not present in the Trie
            print("The query string is not present in the Trie")