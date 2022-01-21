print('What is the temperature in fahrenheit?')
fahrenheit = input()
if fahrenheit.isdecimal() == False:
    print('Input is not a number.')
    exit()
fahrenheit = int(fahrenheit)
celsius = (fahrenheit - 32) * 5/9
celsius = int(celsius)

print('Temperature in celsius is ', celsius)