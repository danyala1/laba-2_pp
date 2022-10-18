import os
from typing import Optional

import csv


def second_script(path: str) -> str:
    #read csv and copy dataset .../1/0001.txt =.../1_0001.txt
    with open("classmates.csv", "r") as fh:
        reader = csv.reader(fh)  # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    if os.path.isdir("second_dataset") == False: os.makedirs("second_dataset")
    content = False
    for element in spisok:
        if content:
            with open(element[0], "rb") as f:
                text = f.read()
                namefile = element[1].split("/")
            with open(os.path.join("second_dataset", element[2] + "_" + namefile[2]), "wb") as f:
                f.write(text)
        content = True

def iterator2(name: str) -> Optional[str]:
    '''create a csv'''
    names = os.listdir(os.path.join("dataset", name))
    for i in range(len(names)):
        yield (names[i]) # делаем итератор
    return None


class Iterator2_txt:
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


def script_2(name: str) ->None:
    '''create a csv'''
    second_script(name)

if __name__=="__main__":
    script_2("rt")