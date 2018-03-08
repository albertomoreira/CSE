# Defining functions
def hello_world():
    print("Hello World!")


hello_world()


def square_it(number):
    return number ** 2


print(square_it(3))


def tip_calc(subtotal):
    tax_amt = subtotal * 0.18
    return tax_amt


def total_bill(bill_amt):
    total = bill_amt + tip_calc(bill_amt)
    print("Your total bill %d" % total)


total_bill(100)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


print(distance(0, 0, 3, 4))


def pythagorean(a, b):
    inside = (a ** 2 + b ** 2)
    answer = inside ** 0.5
    return answer


print(pythagorean(5, 12))
