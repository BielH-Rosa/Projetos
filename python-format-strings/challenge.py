first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.rstrip()
first_value = first_value.title()
# Second challenge
second_value = second_value.replace('-', '').lstrip().capitalize()

# Third challenge
third_value = third_value.replace(' ', '').replace('-', ' ').swapcase()


print(first_value.rjust(22))
print(second_value)
print(third_value.rjust(30))

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')