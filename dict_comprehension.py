from pprint import pprint as pp
#Noticed - pprint is printing dict by alphabetic order by key

'''
{
    key_expr(item): value_expr(item)
    for item in iterable
}
'''

country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brasilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'
                      }

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

pp(country_to_capital)

pp(capital_to_country)

# for key, value in capital_to_country.items():
#     print(f'{key} = {value}\n')

sentence = 'hej mistrzu, czy to czas na zwycięstwo ?'
words = sentence.split()
words = {x[0] + '!': x for x in words}
print(words)
