n = int(input('Enter any number: '))
if(n > 0 and n < 101):
    print('The number {} is between 1 and 100'.format(n))
else:
    print('{} is not between 1 and 100'.format(n))