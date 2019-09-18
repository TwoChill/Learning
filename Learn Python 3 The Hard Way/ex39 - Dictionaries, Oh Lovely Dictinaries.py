# creates a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print(states)
# create a basic set of staters and some cities in them

cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
print(cities)

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print(cities)
print('\n')

print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])
print('\n')

# print some staters
print('Michigan abbreviation is: ', states['Michigan'])
print('Florida abbreviation is: ', states['Florida'])
print('\n')

# do it by using state then cities dict
print('Florida has: ', cities[states['Florida']])
print('Michigan has: ', cities[states['Michigan']])
print('\n')

# print every state
for state, abbr in states.items():
    print(state, 'abbreviation', abbr)
print('_' * 25, '\n', 'Book example:')
for state, abbr in list(states.items()):
    print(f'{state} is abbreviation {abbr}')
print('\n')

# print every city
for abbr, city in cities.items():
    print(abbr, 'has the city:', city)
print('_' * 25, '\n', 'Book example:')
for city, abbr in list(cities.items()):
    print(f'{abbr} has the city: {city}')
print('\n')

# no do both at the same time
for state, abbr in states.items():
    print(f'{state} stare is abbreviation {city}')
    print(f'and has city {cities[abbr]} \n')
print('\n')

# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print('Sorry, no Texas')
print('\n')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f'The city for thatstate "TX" is : {city}')
