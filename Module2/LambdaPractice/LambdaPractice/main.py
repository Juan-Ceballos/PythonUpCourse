# anonymous functions that are nameless guessing swift closures

def greeting(x):
    return x
print(greeting("Hello World"))

a = lambda b: b

print(a("Hello World 2"))

def multiplication(x, y):
    return x * y

print(multiplication(2, 3))

product = lambda num1, num2: num1 * num2

print(product(2, 5))

# combine def and lambda

def multiplication_lambda(c):
    return lambda d: d * c

product2 = multiplication_lambda(2)
print(product2(9))

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

validNums = list(filter(lambda number: number % 2 == 0, num_list))

print(validNums)
