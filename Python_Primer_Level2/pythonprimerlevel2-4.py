print ("I'm not a function")

def my_function():
    print("Hey I'm a function!")

def brett(val):
    for i in range(val):
        print("I'm a function with args!")

def my_sum(val):
    total = 0
    for i in range(val):
        total = total + i + 1
    return total

my_function()
brett(5)
print(my_sum(3))
