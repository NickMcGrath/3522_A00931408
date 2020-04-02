"""
A basic calculator using command prompt.

ladjfasdflkasdjfklajsdflkjaslkdjflaksjdfkljasldkjfajsdflkjasldfjalskjdflakjsdflkjasldfkjklsdjfkasjdfasdf;a
"""
MEME = 9


def add(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return (
            a + b
    )


def subtract(a, b):
    return a - b


def divide(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a / b


def multiply(a, b):
    return a * b


def main():
    input_map = {
        '+': add,
        '-': subtract,
        '/': divide,
        '*': multiply
    }
    operator = input("Type an operator or 0 to exit: ")
    while operator != '0':
        print("type 2 values")
        a = int(input("enter first value: "))
        b = int(input("enter second value: "))
        print(input_map[operator](a, b))
        operator = input("Type an operator or 0 to exit: ")


if __name__ == '__main__':
    main()
