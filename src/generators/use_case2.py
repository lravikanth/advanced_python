# if its simple we can use list comprehensions
# if more data gen comprehensions are use fill


from typing import Generator


def ex_gen_comp():
    # list comp. this creates all elements in memory
    squares = [x * x for x in range(5)]
    # replace sq brackets with round. They become gen comp
    # elements are not created until next or looped thru
    squares_gen = (x * x for x in range(5))

    sum_sqs = fn_sum(x * x for x in range(10))
    print(sum_sqs)


def fn_sum(fn: Generator[int, None, None]) -> int:
    total = 0
    for i in fn:
        total = total + i
    return total


ex_gen_comp()

# THIS IS BEST USE CASE
# Generators are easy to compose
# we can build pipe lines for data
# read thru sample2 file and give out total of all the valid numbers


def print_gen(fn: Generator):
    for i in fn:
        print(i)


def ex_compose():
    with open("sample2.txt") as file:
        nums = (row.rstrip() for row in file)  # strip of new line /n
        # now loop over above generator to remove empty lines
        nums = (row for row in nums if row)
        # now only grab numbers
        nums = (int(row) for row in nums if not str.isalpha(row))
        # print_gen(nums)
        s = fn_sum(nums)
        print(s)


# above example we dont need more then oneline in memory
ex_compose()
#
