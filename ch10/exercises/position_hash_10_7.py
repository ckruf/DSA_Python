import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from ch08.my_practice_implementations.linked_binary_tree import Position, Node


class HashablePosition(Position):

    def __hash__(self):
        return id(self._node)


def main():
    a = Node("A", None, None, None)
    b = Node("B", None, None, None)

    unhashable_pos_1 = Position(a, None)
    try:
        hash(unhashable_pos_1)
        print("This should not print")
    except TypeError:
        print("This should print, since position should not be hashable")

    hashable_pos_1 = HashablePosition(a, None)
    hashable_pos_2 = HashablePosition(b, None)

    hash_1 = hash(hashable_pos_1)
    hash_2 = hash(hashable_pos_2)

    assert hash_1 != hash_2 

    hashable_pos_1._node._element = "C"

    # hash should stay the same even though node element has changed
    assert hash(hashable_pos_1) == hash_1
    hashable_pos_1._node = b
    # the positions should now have the same has considering they refer to the same node
    assert hash(hashable_pos_1) == hash(hashable_pos_2)
    print("success")


if __name__ == "__main__":
    main()