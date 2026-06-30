def multiply(*args):
    product = 1
    for i in args:
        product = product * i
    return product


print(multiply(1,2,3,4,5,6,78))
