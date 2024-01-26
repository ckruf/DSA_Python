import sys
import os
from pathlib import Path

# add root dir of project to sys path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
script_path = Path(SCRIPT_DIR)
src_dir = script_path.parent.parent.absolute()
print(src_dir)
sys.path.insert(0, str(src_dir))

from typing import Any, Iterator
from ch10.my_practice_implementations.unsorted_table_map import UnsortedTableMap



class ItemsUnsortedTableMap(UnsortedTableMap):

    def items(self) -> Iterator[tuple[Any, Any]]:
        for item in self._table:
            yield item._key, item._value