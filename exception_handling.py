try:
    x = 10/2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')