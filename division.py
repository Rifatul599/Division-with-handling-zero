x = 8
y = 4
try:
    solution = x/y
except ZeroDivisionError :
    print("division by zero!")
else:
    print("Answer is",solution)