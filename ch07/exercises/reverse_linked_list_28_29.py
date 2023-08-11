"""This file contains solution attempts for exercises 7.28 and 7.29"""
from ch07.my_practice_implementations.singly_linked_list import LinkedList, Node


def reverse_list_recursively(L: LinkedList):
    def traverse_reverse_recurse(current_node: Node, prev_node: Node) -> None:
        if current_node is None:
            return
        next_node = current_node._next
        current_node._next = prev_node
        traverse_reverse_recurse(next_node, current_node)

    traverse_reverse_recurse(L._head, None)
    original_head = L._head
    original_tail = L._tail
    L._head = original_tail
    L._tail = original_head


def reverse_list_iteratively(L: LinkedList):
    walk = L._head
    prev = None
    while walk is not None:
        following = walk._next
        walk._next = prev
        prev = walk
        walk = following
    original_head = L._head
    original_tail = L._tail
    L._head = original_tail
    L._tail = original_head
