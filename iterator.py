import os
from typing import Optional

def iterator(name: str) -> Optional[str]:
    """create a csv"""
    names = os.listdir(os.path.join("dataset", name))
    for i in range(len(names)):
        yield (names[i])  # делаем итератор
    return None


class Iterator_txt:
    def __init__(self, name: str):
        self.names = os.listdir(os.path.join("dataset", name))
        self.limit = len(self.names)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration