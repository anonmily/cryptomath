︠6bc16c6f-f3ea-4f7b-877c-323cd173559as︠
import math
import time

def xgcd(a,b):
    # Extended Euclidean Algorithm
    # From: http://anh.cs.luc.edu/331/notes/xgcd.pdf
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = math.floor(a/b)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return (int(a), int(prevx), int(prevy))

def get_mod_inverse(a, m):
    # Use the extended Euclidean algorithm (Algorithm 2.107) to find integers x and y such
    # that ax + ny = d, where d = gcd(a, n).
    xgcd_res = xgcd(a,m)
    d = xgcd_res[0]

    # For a to be invertible, gcd(a,n) == 1
    assert( d == 1 )

    # Return x
    return xgcd_res[1] % m
︡dd484e72-e698-4fc5-8c31-b2dbf8a01dc1︡{"done":true}
︠335536af-1959-4cc4-a2a6-49bf2b064a16s︠
def babygiantstep(p,g,h, use_element_order=False, verbose=False, generate_all=False):
    start_time = time.time()

    if not use_element_order:
        # get the order m = p - 1
        N = p - 1
    else:
        N = int(Mod(g,p).multiplicative_order())
    print 'N=', N
    n = int(math.ceil(math.sqrt(N)))

    # get mod inverse of g
    g_inv = get_mod_inverse(g, p)

    # Compute g^−n
    g_inv_n = pow(g_inv, n, p)

    s = 1
    t = h

    # Use a dictionary/hash for the babystep array
    tbl = {}

    x = None

    if verbose:
        print 'n=', n, 'g_inv=', g_inv,'g_inv_n=', g_inv_n

    i = 0
    while i < n:

        # Save babystep {value => index}
        tbl[s] = i

        # print('i=%s, s=%s, t=%s' % (i,s,t))

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            if verbose: print 'found t=', t, 'i=', i, 'j=', j
            x = i * n + j
            if not generate_all: break

        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

        # Increment counter
        i = i + 1

    end_time = time.time()
    if verbose: print 'Elapsed duration: ', int(end_time - start_time), 'seconds'

    # Return the discovered x
    if x:
        return x
    else:
        raise Exception('No discrete log found for g=%s, h=%s, p=%s' % (g, h, p))
︡7908ce6b-2dc6-4a5b-808f-13a70ac580b0︡{"done":true}
︠b8b49b72-ec29-4edc-b50a-eba002254edas︠
p = 200003000003
g = 3
A = 387420489
B = 131128838694
X = 'HNKFNOJXPQRASSUTRFQGTBKMLRZSJNVHIXYAGVKLLFXHFBGWWJHRJDDXXBJESDYHTFWTNOU'
x = babygiantstep(p,g,A, verbose=True)
print 'x=', x
check_A = pow(g, x, p)
print 'g^x = ', check_A,'= A = ', A, '(', check_A ==  A, ')'
︡44389aeb-713b-4ef7-a23e-95add07cf90e︡{"stdout":"N= 200003000002\nn= 447217 g_inv= 66667666668 g_inv_n= 140173535036\nfound t="}︡{"stdout":" 119505135162 i= 137605 j= 89349\nElapsed duration:  0 seconds\n"}︡{"stdout":"x= 61539384634\n"}︡{"stdout":"g^x =  387420489 = A =  387420489 ( True )\n"}︡{"done":true}
︠696ff100-e74f-4a1e-afb5-535cb3f6d7c7s︠
x = babygiantstep(p,g,A, use_element_order=True, verbose=True)
check_A = pow(g, x, p)
print 'g^x = ', check_A,'= A = ', A, '(', check_A ==  A, ')'
︡ba2187ab-bce7-467b-9759-cfbf46ccaf28︡{"stdout":"N= 7692423077\nn= 87707 g_inv= 66667666668 g_inv_n= 158029923284\nfound t="}︡{"stdout":" 175266719955 i= 87705 j= 80660\nElapsed duration:  0 seconds\n"}︡{"stdout":"g^x =  387420489 = A =  387420489 ( True )\n"}︡{"done":true}
︠055e39e5-df7c-474e-8df5-1293ccfd0671︠
# Testing object pointers and list/set
a = [1,2,3]
id(a)
︡963e73cd-4c8c-476f-9b3e-8979959bd26c︡{"stdout":"140028696281600\n"}︡{"done":true}
︠8f639e15-0558-455c-bba9-e0608e276a4b︠
b = set(a)
id(b)
︡04dc8c5b-4737-4071-9d1d-bee63c9c9335︡{"stdout":"140028696955928\n"}︡{"done":true}
︠39e1b339-44ad-4fe9-8e8f-223feeedf04e︠
id(a)
︡b16e6454-ee44-4f6c-b1c0-4625d5bd76f0︡{"stdout":"140028696281600\n"}︡{"done":true}
︠ce0e4362-3276-4c10-b680-499f504fb673︠









