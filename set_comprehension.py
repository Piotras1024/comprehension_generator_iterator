from math import factorial

f = {len(str(factorial(x))) for x in range(20)}
print(f'f = {f} \nlength of factorial above 1-20\nvariable f is type == {type(f)}')