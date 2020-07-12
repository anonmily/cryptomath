from .divisibility import xgcd
import inspect

def find_x_for_mod(f, c, m, check_neg=False, print_all=False):
    '''
    Given a lambda eq (e.g. lambda x: 6*x), find x such
    that it is congruent to c modulo m.

    When print_all=True, all mod values will be printed
    to console.

    Example: Find x such that:  6x + 50 = 9 (mod 26)
    find_mod(lambda x: 6x+50, c=9, mod=26)
    find_mod(lambda x: 6x+50, c=9, mod=26, print_all=True)
    '''
    x = 0
    c = c % m
    solution = None

    if callable(f):
        f_str = inspect.getsource(f)
    else:
        f_str = f 
        f = lambda x: eval(f_str)

    if print_all:
        print('-----------------------')
        print('{:^10s} {:^10s}'.format('x', 'f(x) mod m') )
        print('-----------------------')

    # Brute force
    while not solution:
        x = x + 1

        # Check positive x
        y = f(x)
        y = y % m
        if y == c: solution = x
        if print_all: print('{:^10n} {:^10n}'.format(x,y) )

        # Check negative x
        if check_neg:
            x_neg = x * -1
            y2 = f(x_neg)
            y2 = y2 % m
            if y2 == c: solution = x_neg
            if print_all: print('{:^10n} {:^10n}'.format(x_neg,y2) )

    if print_all: print('-----------------------')

    print('x = ' + str(solution))

    return solution

def get_mod_inverse(a, m):
    '''
    Find the modular inverse of a modulo m:
    a(a^-1) = 1 (mod m)
    '''
    x = xgcd(a, m)[1]
    return x % m
