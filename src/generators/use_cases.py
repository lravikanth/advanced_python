# generators dont create values upfornt. So memory efficient

# common use case is reading large file(GB) row by row.

from dataclasses import dataclass


@dataclass
class Data:
    a: int
    b: int


def mydata_reader(file):
    for row in file:
        data = row.rstrip().split(",")
        yield Data(data[0],data[1])


def ex_reader():
    with open("sample.txt") as file:
        for row in mydata_reader(file):
            print(row)


ex_reader()

#another use is lazy sequences
#if we return a huge list, its memory intensive.
#using generator is more efficient

