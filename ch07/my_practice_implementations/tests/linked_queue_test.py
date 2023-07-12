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
    """
    Test the 'dequeue()' method of the LinkedQueue class.
    NOTE these tests depend on the enqueue method being implemented correctly.
    """

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
    def test_dequeue_sets_new_head():
        """
        Test that the 'dequeue()' method correctly sets pointer to the new head.
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        B_node = queue._head._next
        queue.dequeue()
        assert queue._head == B_node

    @staticmethod
    def test_dequeue_return():
        """
        Test that the 'dequeue()' method returns the expected element.
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        assert queue.dequeue() == "A"
        assert queue.dequeue() == "B"

    @staticmethod
    def test_dequeue_decrements_size():
        """
        Test that the 'dequeue()' method decrements the size of the queue
        after it is called.
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        assert queue._size == len(queue) == 3
        queue.dequeue()
        assert queue._size == len(queue) == 2
        queue.dequeue()
        assert queue._size == len(queue) == 1
        queue.dequeue()
        assert queue._size == len(queue) == 0
        

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


class TestFront:
    """Tests for the 'front()' method of the LinkedQueue class."""

    @staticmethod
    def test_front_empty():
        """
        Test that an Exception is raised when the 'front()' method is called
        on an empty queue.
        """
        queue = LinkedQueue()
        with pytest.raises(Exception):
            queue.front()

    @staticmethod
    def test_front_non_empty():
        queue = LinkedQueue()
        queue.enqueue("A")
        assert queue.front() == "A"


class TestIsEmpty:
    """Tests for the 'is_empty()' method of the LinkedQueue class."""

    @staticmethod
    def test_is_empty_empty():
        queue = LinkedQueue()
        assert queue.is_empty() is True

    @staticmethod
    def test_is_empty_non_empty():
        queue = LinkedQueue()
        queue.enqueue("A")
        assert queue.is_empty() is False


class TestRotate:
    """Tests for the 'rotate()' method of the LinkedQueue class."""

    @staticmethod
    def test_rotate_empty():
        """
        Test that 'rotate()' method raises Exception when called on
        an empty list.
        """
        queue = LinkedQueue()
        with pytest.raises(Exception):
            queue.rotate()

    @staticmethod
    def test_rotate_single_element():
        """
        Test that 'rotate()' method works correctly on a queue with a single
        element (ie does nothing).
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        A_node = queue._head
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        assert queue._tail == A_node
        queue.rotate()
        assert queue._head == A_node
        assert queue._tail == A_node

    @staticmethod
    def test_rotate_two_element():
        """
        Test that the 'rotate()' method works correctly on a queue with two
        elements.
        """
        queue = LinkedQueue()
        queue.enqueue("A")
        queue.enqueue("B")
        A_node = queue._head
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = queue._tail
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"

        assert A_node._next == B_node
        assert B_node._next is None

        queue.rotate()
        assert queue._head == B_node
        assert queue._tail == A_node
        assert B_node._next == A_node
        assert A_node._next is None

    @staticmethod
    def test_rotate_multiple_elements():
        """
        Test that the 'rotate()' method works correctly on a queue with 
        multiple elements.
        """
        queue = LinkedQueue()
        for e in "A", "B", "C", "D":
            queue.enqueue(e)
        
        A_node = queue._head
        assert isinstance(A_node, _Node)
        assert A_node._element == "A"
        B_node = A_node._next
        assert isinstance(B_node, _Node)
        assert B_node._element == "B"
        C_node = B_node._next
        assert isinstance(C_node, _Node)
        assert C_node._element == "C"

        D_node = queue._tail
        assert isinstance(D_node, _Node)
        assert D_node._element == "D"
        assert D_node._next is None

        queue.rotate()

        assert queue._head == B_node
        assert B_node._next == C_node

        assert D_node._next == A_node

        assert queue._tail == A_node
        assert A_node._next is None
        



class TestGeneral:
    """
    Test a sequence of enqueue and dequeue operations.
    """

    @staticmethod
    def test_general():
        queue = LinkedQueue()
        for i in range(1, 101):
            queue.enqueue(i)
            assert len(queue) == i

        for i in range(1, 101):
            assert queue.front() == i
            assert queue.dequeue() == i
            assert len(queue) == 100 - i

        assert queue.is_empty() is True