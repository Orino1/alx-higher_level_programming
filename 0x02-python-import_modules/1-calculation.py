#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as mud

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, mud.add(a, b)))
    print("{} - {} = {}".format(a, b, mud.sub(a, b)))
    print("{} * {} = {}".format(a, b, mud.mul(a, b)))
    print("{} / {} = {}".format(a, b, mud.div(a, b)))