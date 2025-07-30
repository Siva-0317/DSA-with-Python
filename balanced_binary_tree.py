"""110. Balanced Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0, True

            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)

            height = max(left_height, right_height) + 1
            balanced = (
                left_balanced and right_balanced and abs(left_height - right_height) <= 1
            )

            return height, balanced

        _, is_bal = check(root)
        return is_bal

# Helper function to build tree from list input
def build_tree(nodes):
    from collections import deque
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

# Example usage
if __name__ == "__main__":
    # Change the input list to test different trees
    input_list = [3,9,20,None,None,15,7]  # Try also: [1,2,2,3,3,None,None,4,4]
    root = build_tree(input_list)
    sol = Solution()
    print(sol.isBalanced(root))  # Output: True or False
