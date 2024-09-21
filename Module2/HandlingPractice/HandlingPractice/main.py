# try, except
import math

x = "Hello World"

print(x)

# print(y) gives name error if no y

try:
    print(y)
except:
    print("oops an error has occurred")


try:
    print(z)
except NameError:
    print("var z not defined")
except:
    print("something else went wrong")

try:
    a = math.sqrt(-100)
    print(a)
except NameError:
    print('Variable a not defined')
except ValueError:
    print("Positive number expected for square root operation")

# Also have TypeError
# If else added runs along with the no error route
# finally keyword that executes at end of try/except