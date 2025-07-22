#level order traversal of a binary tree with tree building function
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
# Function to build tree from list
def build_tree(values):
    if not values:
        return None
    root= TreeNode(values[0])
    queue=[root]
    i=1
    while i< len(values):
        current=queue.pop(0)
        if values[i] is not None:
            current.left=TreeNode(values[i])
            queue.append(current.left)
        i+=1
        if i< len(values) and values[i] is not None:
            current.right=TreeNode(values[i])
            queue.append(current.right)
        i+=1
    return root
def levelorder(root):
    result=[]
    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)
    traverse(root)
    return result
# Example usage from user input, user gives null as input for no node handle it properly
if __name__ == "__main__":
    input_values = input("Enter the tree values in level order (use 'null' for no node): ").split(',')
    input_values = [int(x.strip()) if x.strip().lower() != 'null' else None for x in input_values]
    root = build_tree(input_values)
    print("Level Order Traversal:", levelorder(root))  # Output: Level Order Traversal: [1, 2, 3] for the example given