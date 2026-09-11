# iterables - Its some thing looped over
# it will have __iter__ method
# No next method
# loop thru multiple times
# ierator: Has a state where it know where it is in iteration and knows to get next item
# can only loop thru once. Once it hit stopInteration exception.

# Generators are also iterators where next and iter method are impl automatically
# we can only go over generators once


nums = [1, 2, 3]
for num in nums:
    print(num)
