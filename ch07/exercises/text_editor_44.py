import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.absolute()
dsa_python_dir = src_dir.parent.absolute()
sys.path.insert(0, str(dsa_python_dir))

from enum import Enum
from ch07.my_practice_implementations.positional_list import PositionalList, Position


class Cursor:
    pass


class InvalidCommand(Exception):
    pass


class Operation(Enum):
    LEFT = "left"
    RIGHT = "right"
    INSERT = "insert"
    DELETE = "delete"
    EXIT = "exit"


class TextEditor:
    """
    A simple text editor which saves a string of characters and has a cursor.

    Supports the following operations:
    - left: move the cursor one position to the left (do nothing if at beginning)
    - right: move the cursor one position to the right (do nothing if at end)
    - insert: insert given character just after the cursor
    - delete: delete the character just after the cursor (do nothing at end)
    """
    _data: PositionalList
    _cursor_position: Position

    def __init__(self):
        self._data = PositionalList()
        self._cursor_position = self._data.add_last(Cursor())


    def display(self) -> None:
        walk = self._data.first()
        while walk is not None:
            element = walk.element()
            if isinstance(element, Cursor):
                print("|", end="")
            else:
                assert isinstance(element, str)
                print(element, end="")
            walk = self._data.after(walk)
        print()

    def move_left(self) -> None:
        if self._data.first() == self._cursor_position:
            return
        before_cursor = self._data.before(self._cursor_position)
        self._data.delete(self._cursor_position)
        self._cursor_position = self._data.add_before(before_cursor, Cursor())

    def move_right(self) -> None:
        if self._data.last() == self._cursor_position:
            return
        after_cursor = self._data.after(self._cursor_position)
        self._data.delete(self._cursor_position)
        self._cursor_position = self._data.add_after(after_cursor, Cursor())

    def insert(self, char: str) -> None:
        self._data.add_before(self._cursor_position, char)

    def delete_after(self) -> None:
        if self._data.last() == self._cursor_position:
            return
        after_cursor = self._data.after(self._cursor_position)
        self._data.delete(after_cursor)
    
    @staticmethod
    def interpret_command(command: str) -> Operation:
        upper_command = command.upper()
        operation = Operation.__members__.get(upper_command)
        if operation is not None:
            return operation
        raise InvalidCommand(f"{command} is not a valid command")

    def run(self):
        print("Welcome to this useless text editor")
        print("The available commands are:")
        print("- 'left', moves cursor to the left")
        print("- 'right', moves cursor to the right")
        print("- 'insert', inserts character just after cursor")
        print("- 'delete', deletes character just after cursor")
        print("- 'exit', closes the editor")

        while True:
            print("Current text:")
            self.display()
            command = input("Enter command: ")
            try:
                operation = self.interpret_command(command)
            except InvalidCommand as e:
                print(str(e))
                continue
            if operation is Operation.DELETE:
                self.delete_after()
            elif operation is Operation.INSERT:
                new_char = ""
                while len(new_char) != 1:
                    new_char = input("Enter single character: ")
                self.insert(new_char)
            elif operation is Operation.RIGHT:
                self.move_right()
            elif operation is Operation.LEFT:
                self.move_left()
            elif operation is Operation.EXIT:
                break


if __name__ == "__main__":
    editor = TextEditor()
    editor.run()