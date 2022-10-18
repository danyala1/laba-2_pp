import csv


def forteen_script(star):
    # print directorys on star
    with open("classmates.csv", "r") as fh:
        reader = csv.reader(fh) # (!) обратите внимание, что reader возвращает итератор
        spisok = list(reader)  # поэтому мы делаем приведение к типу list
    for element in spisok:
        if element[2] == str(star): print(element[0])


if __name__=="__main__":
    forteen_script(2)