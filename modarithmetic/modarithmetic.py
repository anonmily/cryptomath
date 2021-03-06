import inspect
from .divisibility import xgcd

def find_x_for_mod(f, c, m, check_neg=False, verbose=False):
    '''
    Given a lambda eq (e.g. lambda x: 6*x), find x such
    that it is congruent to c modulo m.

    When print_all=True, all mod values will be printed
    to console.

    Example: f(x) = 5x === 4 (mod 3)
    f = lambda x: 5*x 
    x = find_x_for_mod(f, c=4, m=3, print_all=True)
    '''
    x = 0
    c = c % m
    solution = None

    if callable(f):
        f_str = inspect.getsource(f)
    else:
        f_str = f 
        f = lambda x: eval(f_str)

    if verbose:
        print('-----------------------')
        print('{:^10s} {:^10s}'.format('x', 'f(x) mod m') )
        print('-----------------------')

    # Brute force
    while not solution and x <= m:
        x = x + 1

        # Check positive x
        y = f(x)
        y = y % m
        if y == c: solution = x
        if verbose: print('{:^10n} {:^10n}'.format(x,y) )

        # Check negative x
        if check_neg:
            x_neg = x * -1
            y2 = f(x_neg)
            y2 = y2 % m
            if y2 == c: solution = x_neg
            if verbose: print('{:^10n} {:^10n}'.format(x_neg,y2) )

    if verbose: print('-----------------------')

    print('x = ' + str(solution))
    if not solution: 
        raise Exception(f'No solution found for: {f_str} === {c}, (mod {m})')

    return solution

def get_mod_inverse(a, m):
    '''
    Find the modular inverse of a modulo m:
    a(a^-1) = 1 (mod m)
    '''
    x = xgcd(a, m)[1]
    return x % m