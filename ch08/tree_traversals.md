# Tree traversal algorithms

A traversal of a tree is a systematic way of accessing or "visiting" all its positions.

There are several common traversal schemes for trees, each with its own applications. These include:
- preorder traversals
- postorder traversal
- breadth-first traversal
- in-order traversal (binary tree only)

## Preorder traversal

In a preorder traversal, the current node is processed before ("pre") the traversals of its children, that's why it's called a preorder traversal.

The process can be summarized in these steps:
- process the current node
- recursively traverse and process its children 

The pseudocode would look something like this:

```
def preorder(T: Tree, p: Position):
    perform action on position p
    for child in T.children(p):
        preorder(T, child)
```

The traversal looks like this when visualized:

<img src="./preorder_traversal.png">

## Postorder traversal

In a postorder traversal, the current node is processed after ("post") the traversals of its children, that's why it's called a postorder traversal.

The process can be summarized in these steps:
- recursively traverse and process the node's children 
- process the current node

The pseudocode would look something like this:

```
def postorder(T: tree, p: Position):
    for child in T.children(p):
        postorder(child)
    perform action on position p
```

The traversal looks like this when visualized:

<img src="./postorder_traversal.png">

