# Python3 program to for tree traversals

# students class that represents an individual node in a
# Binary Tree


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# students function to do inorder tree traversal
def printInorder(root):

	if root:
		# First recur on left child
		printInorder(root.left)
		# then print the data of node
		print(root.val)
		# now recur on right child
		printInorder(root.right)


# students function to do preorder tree traversal
def printPreorder(root):
	if root:
		# First print the data of node
		print(root.val)
		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# students function to do postorder tree traversal
def printPostorder(root):
	if root:
		# First recur on left child
		printPostorder(root.left)

		# then recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	printInorder(root)
	print ("---------------------")
	printPreorder(root)
	print("---------------------")
	printPreorder(root)