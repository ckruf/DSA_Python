# The `after` method in a binary tree


The `after` method in a binary (search) tree, given a position p, should return the position which comes after p in an inorder traversal.

Let's first remind ourselves of the definition of an inorder traversal:

```
def inorder(self, p):
    if self.left(p) is not None:
        inorder(self.left(p))
    perform visit action for p
    if self.right(p) is not None:
        self.inorder(self.right(p))
```

The inorder traversal obviously first visits the left subtree, then it visits the node, and then it visits the right subtree.

The implementation of `after` distinguishes between two cases:

- p has a right child 
- p does not have a right child

If p does have a right child, then the next position is the leftmost positon of the right subtree.

If p does not have a right child, then that must mean that p is the furthest right child in a particular subtree. Therefore, the next node after p in an inorder traversal is the parent of the root node of the subtree. How do find that node? Well, if p is the node that we get to if we keep going right in a given subtree, then the root of that subtree must be a left child. So we continue up the tree until we find a left child, and then its parent must be the next node in an inorder traversal.
