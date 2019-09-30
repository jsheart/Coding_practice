# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def remove_extra_edge_BT(root):
	seen = {root}
	q = deque([root])
	while q:
		found = False
		for _ in range(len(q)):
			cur = q.popleft()
			if cur.left not in seen:
				seen.add(cur.left)
				q.append(cur.left)
			else:
				print([cur.val, cur.left.val])
				cur.left = None
				found = True
				break
			if cur.right not in seen:
				seen.add(cur.right)
				q.append(cur.right)
			else:
				print([cur.val, cur.right.val])
				cur.right = None
				found = True
				break
		if found:
			break

def remove_extra_edge_BST(root):
	def remove_extra_edge_BST(node, min, max):
		if not node:
			return None
		if (min and node.val <= min) or (max and node.val >= max):
			return None
		if node.left:
			node.left = remove_extra_edge_BST(node.left, min, node.val)
			if not node.left:
				print(node.val)
		if node.right:
			node.right = remove_extra_edge_BST(node.right, node.val, max)
			if not node.right:
				print(node.val)
		return node
	remove_extra_edge_BST(root, None, None)

if __name__ == '__main__':
	root = TreeNode(1)
	node1 = TreeNode(2)
	node2 = TreeNode(3)
	node3 = TreeNode(4)
	node4= TreeNode(5)
	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node4
	remove_extra_edge_BT(root)
	
	root = TreeNode(3)
	node1 = TreeNode(2)
	node2 = TreeNode(5)
	node3 = TreeNode(1)
	node4= TreeNode(4)
	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node4
	remove_extra_edge_BST(root)