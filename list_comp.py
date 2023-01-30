'''
General form of list Comprehension
[expression(item) for item in iterable]
'''


'''

Easy example to use LIST COMPREHENSION

words = 'Wlaz kotek na plotek i mruga. Ladna to piosenka ale niedluga'
list_of_words = words.split()

print([len(word) for word in list_of_words])
'''

from math import factorial

f = [len(str(factorial(x))) for x in range(20)]
print(f'f = {f} \nlength of factorial above 1-20\nvariable f is type == {type(f)}')
