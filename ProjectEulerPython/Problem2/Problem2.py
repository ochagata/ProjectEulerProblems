__author__ = 'Ozer'

LIMIT = 4000000


def get_sum_of_even_fib():
    a = 1
    b = 2

    sum_of_even_terms = b

    term_tracker = 0

    while a <= LIMIT:
        c = a + b
        term_tracker += 1
        if term_tracker == 3:
            sum_of_even_terms += c
            term_tracker = 0
            
        a = b
        b = c

    return sum_of_even_terms

print(get_sum_of_even_fib())