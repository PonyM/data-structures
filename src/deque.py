"""Create a deque to inhereit from doubly linked list."""
from dll import DoubleLink


class Deque(object):
    """Create a deque and associated functions.

    append(val) adds a value to the end of the deque.

    appendleft(val) adds a value to the front of the deque.

    pop() removes a value from the end of the deque and returns it.

    popleft() removes and returns the value at the front of the deque.

    peek() returns the value after the value that would be returned by pop.

    peekleft() returns the value that would be returned by popleft.()

    size() returns the number of nodes in the deque."""

    def __init__(self, head=None, iterable=None):
        """Creating instances for the deque."""
        self._deque = DoubleLink(head, iterable)

    def size(self):
        """Returning the length of the deque in number of nodes."""
        if self._deque.head:
            return self._deque._length
        return 0