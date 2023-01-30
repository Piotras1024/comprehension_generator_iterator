'''
    >> any([False, False, True)
    >> True

    >> all([False, False, True)
    >> False
    >> ([False, False, False)
    True
    sum()
    enumuerate()

    zip()

    global zip()
    sunday = [ 12, 13, 14, 15 ]
    monday = [6, 7, 8, 9 ]
    tuesday = [3, 4, 5, 6]
    global zip() end
    ##

    for item in zip(sunday, monday):
        print(item)

    >> (12, 6)
    >>(13, 7)
    >>(14, 8)
    >>(15, 9)
    ##

    ##

    for sun, mon in zip(sunday, monday):
    print(f"average = {(sun+mon)/2}")

    >>average = 9.0
    >>average = 10.0
    >>average = 11.0
    >>average = 12.0
    ##

    for sun, mon in zip(sunday, monday, tuesday):
        print(f'min = {min(temps):4.1f}, max = {max(temps):4.1f, average = {(sum(temps)/3)}')
    min(), max()

    ##

for temps in zip(sunday, monday, tuesday):
    print(f'min = {min(temps):4.1f}, max = {max(temps):4.1f}, average = {(sum(temps) / len(temps)):4.1f}')

    >>min =  3.0, max = 12.0, average =  7.0
    >>min =  4.0, max = 13.0, average =  8.0
    >>min =  5.0, max = 14.0, average =  9.0
    >>min =  6.0, max = 15.0, average = 10.0

    ##


    def chain(*iterables):
        # chain('ABC', 'DEF') --> A B C D E F
        for it in iterables:
            for element in it:
                yield element


    from itertools import chain
    chain()

    temperatures = chain(monday,tuesday, sunday)
    all(tem > 0 for tem in temperatures)

    >>True

    ##

    def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


    chain.from_iterable(iterable) >> chain for only one iterable

    ##
'''
