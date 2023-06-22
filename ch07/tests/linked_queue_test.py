import pytest
from ch07.my_practice_implementations.linked_queue import _Node, LinkedQueue


class TestInit:
    """Test the __init__() method of the LinkedQueue class"""

    @staticmethod
    def test_init():
        queue = LinkedQueue()
        assert queue._head is None
        assert queue._tail is None
        assert queue._size == 0


class TestEnqueue:
    """Test the 'enqueue()' method of the LinkedQueue class"""

    @staticmethod
    def test_enqueue_when_empty():
        """
        Test the enqueue method when enqueueing into an initially empty queue.
        This is a special case, where we need to point the _head attribute
        to the newly inserted Node. 
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        assert queue._head._element == "A"
        assert queue._tail._element == "A"
        assert queue._head == queue._tail
    
    @staticmethod
    def test_enqueue_non_empty_complete():
        """
        Test the enqueue method when enqueueing into a queue which is not empty.
        Test that:
        - tail is set to inserted node
        - the old tail is pointing to the current tail
        - size has incremented 
        """
        queue = LinkedQueue()
        assert len(queue) == queue._size == 0
        queue.enqueue("A")
        queue.enqueue("B")
        assert len(queue) == queue._size == 2
        assert queue._tail._element == "B"
        assert queue._head._next == queue._tail
        assert queue._head._next == queue._tail

    @staticmethod
    def test_enqueue_non_empty_sets_tail():
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        assert queue._tail._element == "C"

    @staticmethod
    def test_enqueue_non_empty_updates_old_tail_pointer():
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        B_node = queue._head._next
        assert B_node._next is None
        queue.enqueue("C")
        assert isinstance(B_node._next, _Node)
        assert B_node._next._element == "C"

    @staticmethod
    def test_enqueue_increments_length():
        queue = LinkedQueue()
        assert len(queue) == queue._size == 0
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        assert len(queue) == queue._size == 3


class TestDequeue:
    """Test the 'dequeue()' method of the LinkedQueue class."""

    @staticmethod
    def test_dequeue_empty():
        """
        Test that the 'dequeue()' method raises an exception when attempting
        to dequeue from an empty queue.
        """
        queue = LinkedQueue()
        with pytest.raises(Exception):
            queue.dequeue()

    @staticmethod
    def test_dequeue_multiple_complete():
        """
        Test the 'dequeue()' method when called on a queue
        with mulitple elements
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        A_node = queue._head
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert len(queue) == queue._size == 3
        element = queue.dequeue()
        
        # check correct element returned
        assert element == "A"
        # check _head updated
        assert queue._head == B_node
        # check size decrements
        assert len(queue) == queue._size == 2

    @staticmethod
    def test_dequeue_single():
        """
        Test the 'dequeue()' method when called on a queue with a single
        element. This is a special case, _tail must be set to None!
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        assert queue._head is not None
        assert queue._tail is not None
        assert len(queue) == queue._size == 1
        element = queue.dequeue()
        assert element == "A"
        assert queue._head is None
        assert queue._tail is None
        assert len(queue) == queue._size == 0
