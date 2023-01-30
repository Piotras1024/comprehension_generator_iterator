'''
Why some of use returns only first element multiply times (noticed when i define iterator in loop)
Why some of use returns properly ( noticed when i define iterator before loop)


'''


def first(any_iterable):
    this_iterator = iter(any_iterable)
    try:
        return next(this_iterator)
    except StopIteration:
        return False


iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = iter(iterable)

# for index, _ in enumerate(iterable):
#     print(first(iterable))

for index, _ in enumerate(iterable):
    print(next(iterator))

# for index, _ in enumerate(iterable):
#     print(next(iter(iterable)))

