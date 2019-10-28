def foo(s):
    n = int(s)
    assert n != 0, 'n is Zero'
    return 10 / n


def main():
    foo('0')


main()

