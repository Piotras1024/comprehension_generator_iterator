'''
My first generator
The goal is to print all numbers from number to 1

generators :
    lazy evaluation
    itrables define by functions
    Possible to model sequence with no end
    Composable into pipelines

    They have to have:
    include at least one yield statement.
    Return sends a specified value back to its caller whereas Yield can produce
    a sequence of values. We should use yield when we want to iterate over a sequence,
    but don't want to store the entire sequence in memory. Yield are used in Python generators.

    Return wysyła określoną wartość z powrotem do wywołującego, podczas gdy Yield może
    wygenerować sekwencję wartości. Powinniśmy używać yield, gdy chcemy iterować po sekwencji,
    ale nie chcemy przechowywać całej sekwencji w pamięci. Yield są używane w generatorach Pythona.

    What is a sequence of values Python?
    Sekwencja
    A sequence is a succession of values bound together by a container that reflects their type.
    Almost every stream that you put in Python is a sequence. Types of Sequences. Lists.

    generators have same syntax form as list comprehension

    They may:
    include return statements

    Generator functions describe sequences imperatively

    Generator functions contain at least one yield

    Generators are iterators

    Each call to a generator function prodcues a new generator object

    Generators maintain explicit internal state
    Generatory utrzymują jawny stan wewnętrzny >> znają ostatni wynik i na podstawie tego obliczają aktualny obiekt.

    Generators yield values lazily
    Return sends a specified value back to its caller whereas Yield can produce a sequence of values.


'''


def generator_1(number: int):
    while number > 0:
        print('yield soon')
        yield number
        print('after yield')
        number = number - 1
        print('number is lowered by 1')


# generator = generator_1(1000)
# # for i in generator:
# #     print(i)
# #
# tab = [1000]
# while tab[-1] != 1:
#     tab.append(generator_1(tab[0]))

#Generator Expressions
#func (expr(item) for item in iterable)

milion_square = (x*x for x in range(1, 1000001))
print(type(milion_square))

#To recreate a generator from a generator expression, you must execute the expression again.