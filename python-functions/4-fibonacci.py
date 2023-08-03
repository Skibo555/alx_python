#!/usr/bin/python
def fibonacci_sequence(n):

    n_1, n_2 = 0, 1
    count = 0

    if n < 0:
        return n
    elif n == 1:
        return n_1
    else:
        while count < 0:
            print(n_1)
            fib = n_1 + n_2
            n_1 = n_2
            n_2 = fib
            count += 1
            return (count)        