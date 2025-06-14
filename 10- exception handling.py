
try:
    print(x)
except NameError as er:
    print('Something went wrong')
    print(er)
finally:
    print('Finished')

x = input()
if not type(x) is str:
    raise TypeError('Not an integer')