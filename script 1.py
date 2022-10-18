import os
from typing import Optional

import csv
from tqdm import trange


def first_script(path_dir: str) -> None:
    """create csv """
    out_directory = os.path.dirname(__file__)
    with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь к файлу", "Относительный путь к файлу", "номер звезды"])
        for star in trange(1, 6):
            directory = os.path.join(out_directory, "dataset", str(star))
            for dirs, folder, files in os.walk(directory):
                for element in files:
                    file_writer.writerow([str(dirs) + "/" + element, "dataset"+'/' + str(star) + "/" + element, star])

def iterator1(name: str) -> Optional[str]:
    """create a csv"""
    names = os.listdir(os.path.join("dataset", name))
    for i in range(len(names)):
        yield (names[i])  # делаем итератор
    return None

class Iterator1_txt:
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