import pytest
from ch07.my_practice_implementations.circular_queue import CircularQueue, _Node


class TestEnqueue:
    """
    Tests for the 'enqueue()' method of the CircularQueue class
    """

    @staticmethod
    def test_enqueue_empty():
        """
        Test the enqueue method when inserting into an initially empty
        queue. This is a special case, as the _next pointer of the 
        newly inserted element needs to point at itself.
        """
        queue = CircularQueue()
        queue.enqueue("A")
        A_node = queue._tail
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert A_node._next == A_node

    @staticmethod
    def test_enqueue_non_empty():
        queue = CircularQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        C_node = queue._tail
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        A_node = C_node._next
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert B_node._next == C_node

    @staticmethod
    def test_enqueue_increments_size():
        queue = CircularQueue()
        assert queue._size == len(queue) == 0
        queue.enqueue("A")
        assert queue._size == len(queue) == 1
        queue.enqueue("B")
        assert queue._size == len(queue) == 2
        queue.enqueue("C")
        assert queue._size == len(queue) == 3


class TestDequeue:
    """
    Tests for the 'dequeue()' method of the CircularQueue class.
    """

    @staticmethod
    def test_dequeue_empty():
        """
        Test that an exception is raised when calling dequeue on an empty queue.
        """
        queue = CircularQueue()
        with pytest.raises(Exception):
            queue.dequeue()

    @staticmethod
    def test_dequeue_single():
        """
        Test the 'dequeue()' method when the queue contains a single element.
        This is a special case, 'tail' must be set to None
        """
        queue = CircularQueue()
        queue.enqueue("A")
        queue.dequeue()
        assert queue._tail is None

    @staticmethod
    def test_dequeue_mulitple():
        """
        Test the 'dequeue()' method when the queue initially contains multiple
        elements.
        """
        queue = CircularQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        # initial assertions about the three nodes
        C_node = queue._tail
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        A_node = C_node._next
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        assert len(queue) == queue._size == 3
        
        # assertions after dequeue operation
        assert queue.dequeue() == "A"
        # tail should stay the same
        assert queue._tail == C_node
        # but _next pointer of tail should be updated 
        assert C_node._next == B_node
        
        assert len(queue) == queue._size == 2

class TestRotate:
    """
    Tests for the 'rotate()' emthod of the CircularQueue class.
    """

    @staticmethod
    def test_rotate_empty():
        queue = CircularQueue()
        with pytest.raises(Exception):
            queue.rotate()

    @staticmethod
    def test_rotate_single():
        queue = CircularQueue()
        queue.enqueue("A")
        A_node = queue._tail
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        queue.rotate()
        assert queue._tail == A_node

    @staticmethod
    def test_rotate_multiple():
        queue = CircularQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")

        # initial assertions about the three nodes
        C_node = queue._tail
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"
        A_node = C_node._next
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        
        queue.rotate()
        assert queue._tail == A_node


class TestGeneral:
    """
    Test a sequence of enqueue and dequeue operations
    """

    @staticmethod
    def test_general():
        queue = CircularQueue()
        elems = [i for i in range(1, 101)]
        for elem in elems:
            queue.enqueue(elem)
            assert len(queue) == elem
            assert queue.first() == 1
        for elem in elems:
            assert elem == queue.first()
            assert elem == queue.dequeue()

        assert queue.is_empty() is True

                 