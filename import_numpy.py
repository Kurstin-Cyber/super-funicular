#def increment(number, by):
    #return number + by


#print(increment(2, by=1))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

multiply(4, 5, 5, 6, 2)
