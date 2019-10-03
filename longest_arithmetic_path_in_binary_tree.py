class TreeNode:
      def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            
def longest_arithmetic_path(root):
      result = [0]
      def longest_arithmetic_path(node, diff, cur_result, result):
            result[0] = max(result[0], cur_result)
            if node.left: 
                  if diff and node.val - node.left.val != diff:                      
                        cur_result = 0
                  diff = node.val - node.left.val 
                  longest_arithmetic_path(node.left, diff, cur_result + 1, result)
            if node.right: 
                  if diff and node.val - node.right.val != diff:
                        cur_result = 0
                  diff = node.val - node.right.val
                  longest_arithmetic_path(node.right, diff, cur_result + 1, result)
      longest_arithmetic_path(root, None, 1, result)
      return result[0]

if __name__ == '__main__':
      root = TreeNode(2)
      node1 = TreeNode(4)
      node2 = TreeNode(5)
      node3 = TreeNode(6)
      node4 = TreeNode(7)
      node5 = TreeNode(8)
      root.left = node1
      root.right = node2
      node1.left = node3
      node1.right = node4
      node3.right = node5
      print(longest_arithmetic_path(root))           
                  