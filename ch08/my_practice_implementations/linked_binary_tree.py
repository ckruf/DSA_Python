"""File containing my implementation of a linked binary tree"""
from __future__ import annotations

import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
sys.path.insert(0, str(src_dir))

from dataclasses import dataclass
from typing import Any, Optional, Iterator

from ch08.my_practice_implementations.abstract_bin_tree import BinaryTree
from ch08.my_practice_implementations import abstract_tree
from collections import deque



@dataclass(slots=True)
class Node:
    _element: Any
    _parent: Optional[Node]
    _left: Optional[Node]
    _right: Optional[Node]


@dataclass(slots=True)
class Position(abstract_tree.Position):
    _node: Optional[Node]
    _container: LinkedBinaryTree

    def element(self) -> Any:
        return self._node._element

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self._node is other._node


class LinkedBinaryTree(BinaryTree):
    _root: Optional[Node] = None
    _size: int = 0

    def _validate(self, p: Position) -> Node:
        if not isinstance(p, Position):
            raise TypeError(f"p must be a Position, not {type(p)}")
        if p._container is not self:
            raise ValueError("p is not part of this tree")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node: Optional[Node]) -> Optional[Position]:
        if node is None:
            return None
        return Position(node, self)

    def root(self) -> Optional[Position]:
        return self._make_position(self._root)

    def parent(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p: Position) -> int:
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def __len__(self) -> int:
        return self._size

    def left(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p: Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._right)

    def _add_root(self, e: Any) -> Position:
        if self._root is not None:
            raise ValueError("tree already has root")
        root_node = Node(e, None, None, None)
        self._root = root_node
        self._size = 1
        return self._make_position(root_node)

    def _add_left(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("p already has left child")
        left_child = Node(e, node, None, None)
        node._left = left_child
        self._size += 1
        return self._make_position(left_child)

    def _add_right(self, p: Position, e: Any) -> Position:
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("p already has right child")
        right_child = Node(e, node, None, None)
        node._right = right_child
        self._size += 1
        return self._make_position(right_child)

    def _replace(self, p: Position, e: Any) -> Any:
        node = self._validate(p)
        original = node._element
        node._element = e
        return original

    def _delete(self, p: Position) -> Any:
        """
        Delete given node and replace it with its child, if it has a child.
        Raise ValueError if the given node has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Cannot delete node with two children")
        child = node._left or node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(
        self,
        p: Position,
        t1: Optional[LinkedBinaryTree],
        t2: Optional[LinkedBinaryTree]
    ) -> None:
        """
        Attach 
        - tree t1 as left child of given position
        - tree t2 as right child of given position
        
        Note that the left and/or right child position must be empty if you
        want to attach tree.

        Attaching the trees will empty the original trees.
        """
        node = self._validate(p)
        if not type(self) is type(t1) is type(t2):
            raise TypeError("t1 and t2 must be LinkedBinaryTree instances")
        size_t1 = len(t1) if t1 is not None else 0
        size_t2 = len(t2) if t2 is not None else 0
        if t1 is not None and not t1.is_empty():
            if self.left(p) is not None:
                raise ValueError("given position can't have left child if you want to attach t1")
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
        if t2 is not None and not t2.is_empty():
            if self.right(p) is not None:
                raise ValueError("given position can't have right child if you want to attach t2")
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
        
        self._size += (size_t1 + size_t2)

    def positions(self) -> Iterator[Position]:
        return self.inorder()

    def _delete_subtree(self, p: Position) -> None:
        """
        Delete the subtree rooted at position p (including p):
        - update _size
        - set node._parent to node to indicate that the node
        is deprecated 
        - set left, right and element to None, for garbage collection
        I wonder whether this has to be done as a postorder traversal,
        or whether it can be done as a preorder traversal...
        """
        def _recurse_delete(p: Position) -> int:
            sub_total = 0
            for c in self.children(p):
                sub_total += _recurse_delete(c)
            node = self._validate(p)
            node._left = None
            node._right = None
            node._element = None
            node._parent = node
            return sub_total + 1

        if p == self.root():
            self._root = None
        else:
            parent = self.parent(p)
            parent_node = self._validate(parent)
            if self.left(parent) == p:
                parent_node._left = None
            elif self.right(parent) == p:
                parent_node._right = None
        deleted_count = _recurse_delete(p)
        self._size -= deleted_count

    def _swap(self, p: Position, q: Position) -> None:
        """
        Swap the subtree rooted at p with the subtree rooted at q.
        """
        p_node = self._validate(p)
        q_node = self._validate(q)

        p_parent_pos = self.parent(p)
        q_parent_pos = self.parent(q)

        p_parent_node = self._validate(p_parent_pos)
        q_parent_node = self._validate(q_parent_pos)

        p_is_parent_of_q = q_parent_pos == p
        q_is_parent_of_p = p_parent_pos == q

        p_is_left_child = self.left(p_parent_pos) == p
        q_is_left_child = self.left(q_parent_pos) == q

        # handle special case where nodes are adjacent
        if p_is_parent_of_q or q_is_parent_of_p:
            if p_is_parent_of_q:
                p_node._parent = q_node
                q_node._parent = p_parent_node
                if p_is_left_child:
                    p_parent_node._left = q_node
                else:
                    p_parent_node._right = q_node
                if q_is_left_child:
                    q_node._left = p_node
                    p_node._left = None
                else:
                    q_node._right = p_node
                    p_node._right = None
            # q is parent of p
            else:
                p_node._parent = q_parent_node
                q_node._parent = p_node
                if p_is_left_child:
                    p_node._left = q_node
                
                      
        else:
            # set parent pointers of the two nodes
            p_node._parent = q_parent_node
            q_node._parent = p_parent_node

            # set left or right pointer of the nodes' parents
            p_is_left_child = self.left(p_parent_pos) == p
            q_is_left_child = self.left(q_parent_pos) == q
            if p_is_left_child:
                p_parent_node._left = q_node
            else:
                p_parent_node._right = q_node
            if q_is_left_child:
                q_parent_node._left = p_node
            else:
                q_parent_node._right = p_node

    def swap_github(self,p,q):
      """Node referenced by p takes position q and node referenced by
      q takes position p"""
      """There are many special cases to consider"""
      node1 = self._validate(p)
      node2 = self._validate(q)
      if node1._parent == node2._parent: # both children of the same node
          l = node1._left				# mark node1 children 
          r = node1._right
          node1._left = node2._left			# start adjusting the pointers
          if node2._left is not None:		# has node2 any children
              node2._left._parent = node1	
          node1._right = node2._right
          if node2._right is not None:
              node2._right._parent = node1   # they point to node1 now
          node2._left = l   				# adjust node2 pointers
          if l is not None:					# has node1 any children
              l._parent = node2
          node2._right = r
          if r is not None:
              r._parent = node2				# they point to node1 now
          if node1._parent._left == node1:  # node1 was left and node2 was right
              node1._parent._left = node2
              node1._parent._right = node1	# swap positions
              
          else:								# node1 was right and node2 was left
			  
              node1._parent._right = node2
              node1._parent._left = node1	# swap positions
       
      # next case - node2 is a child of node1   
      elif node1._left == node2 or node1._right == node2:
		  # start adjusting node2 pointers
          l = node2._left
          r = node2._right					# mark node2 children
          if node1._left == node2:          # is node2 left child of node1
              node2._left = node1			# now node1 is left child of node2
              node2._right = node1._right	# node1 other child is now node2 right child
              node1._right._parent = node2	# child now points to the right parent
              
          else:								# node2 is right child of node1
			  # adjust pointers as with left child				
              node2._right = node1			
              node2._left = node1._left
              node1._left._parent = node2
          if node1 != self._root:   # node1 has parent
              if node1._parent._left == node1: # is node1 left child
                  node1._parent._left = node2  # now node1 parent points to node2
					
              else:							   # node1 is right child
                  node1._parent._right = node2
          else:								   # node1 is root, it has no parents
              self._root = node2			   # root now is node2
          # start adjusting node1 pointers
          node1._left = l 					  
          if l is not None:			 		   # has node2 any children
              l._parent = node1
          node1._right = r
          if r is not None:
              r._parent = node1				   # they now point to node1
          node2._parent = node1._parent		   
          node1._parent = node2				   # parents now point to the right nodes
         
      else:
		  # non - adjacent nodes, different parents
          l = node1._left
          r = node1._right
          p = node1._parent				# mark node1 attributes
          # start adjusting node1 pointers
          node1._left = node2._left
          if node2._left is not None:		# has node2 any children
            node2._left._parent = node1
          node1._right = node2._right
          if node2._right is not None:
            node2._right._parent = node1    # they now point to node1
  
          node1._parent = node2._parent     
         
          if node2._parent._left == node2:  # is node2 left child of its parent
              node2._parent._left = node1	# parent now points to node1
              
          else:								# node2 is right child
			  
              node2._parent._right = node1
          # adjust node2 pointers
          node2._left = l
          if l is not None:				# has node1 got any children
              l._parent = node2
          node2._right = r
          if r is not None:
              r._parent = node2			# they point to node2 now
          node2._parent = p				
          if p is not None:				# has node1 parent
              if p._left == node1:		# is node1 left child of its parent
                  p._left = node2
              else:						# or node1 is right child
                  p._right = node2		# parent now points to node2
          if node1 == self._root:		# in case node1 is root
              self._root = node2	
            

