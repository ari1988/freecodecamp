try:
    x = 1/0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')

try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f'An error occurred: {e}')
