#Same treee problem
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# Example usage
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Create two sample trees
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

    if is_same_tree(tree1, tree2):
        print("The trees are the same.")
    else:
        print("The trees are not the same.")
        