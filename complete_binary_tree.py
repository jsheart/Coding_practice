from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def is_complete_tree(root):
    if not root:
        return True
    queue = deque([root])
    null_above = False
    while queue:
        length = len(queue)
        for _ in range(length):
            null_left = False
            if queue:
                node = queue.popleft()
                if not node:
                    null_above = True
                    null_left = True
                    continue
                if null_above or null_left:
                    return False
                queue.append(node.left)
                queue.append(node.right)
    return True
        

if __name__ == '__main__':
    tree = '[1,2,3,4,5,6]'
    # tree = '[1,2,3,4,5,null,7]'
    root = stringToTreeNode(tree)
    print(is_complete_tree(root))