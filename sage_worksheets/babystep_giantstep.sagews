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
︡41bcd486-d4b1-4be3-ac14-e702fa49cf47︡{"done":true}
︠335536af-1959-4cc4-a2a6-49bf2b064a16s︠
def babygiantstep(p,g,h, verbose=False, generate_all=False):
    start_time = time.time()

    # get the order m = p - 1
    N = int(math.ceil(math.sqrt(p - 1)))

    # get mod inverse of g
    g_inv = get_mod_inverse(g, p)

    # Compute g^−n
    g_inv_n = pow(g_inv, N, p)

    s = 1
    t = h

    # Use a dictionary/hash for the babystep array
    tbl = {}

    x = None

    if verbose:
        print 'n=', N, 'g_inv=', g_inv,'g_inv_n=', g_inv_n

    for i in range(N):

        # Save babystep {value => index}
        tbl[s] = i

        # print('i=%s, s=%s, t=%s' % (i,s,t))

        # Check if giantstep is in table
        if t in tbl:
            j = tbl[t]
            if verbose: print 'found t=', t, 'i=', i, 'j=', j
            x = i * N + j
            if not generate_all: break

        # Increment values
        s = s*g % p
        t = (t * g_inv_n) % p

    end_time = time.time()
    if verbose: print 'Elapsed duration: ', int(end_time - start_time), 'seconds'

    # Return the discovered x
    if x:
        return x
    else:
        raise Exception('No discrete log found for g=%s, h=%s, p=%s' % (g, h, p))
︡e69d2332-b416-406a-9176-2e9614148245︡{"done":true}
︠b2ff3b0f-8696-43fa-8b33-594a563d5aa4s︠
p = 200003000003
g = 3
A = 387420489
B = 131128838694
X = 'HNKFNOJXPQRASSUTRFQGTBKMLRZSJNVHIXYAGVKLLFXHFBGWWJHRJDDXXBJESDYHTFWTNOU'
x = babygiantstep(p,g,A, verbose=True)
check_A = pow(g, x, p)
print 'g^x = ', check_A,'= A = ', A, '(', check_A ==  A, ')'
︡eba8fcc1-ac5b-49bc-85a7-832e084e0e5b︡{"stdout":"n= 447217 g_inv= 66667666668 g_inv_n= 140173535036\nfound t="}︡{"stdout":" 119505135162 i= 137605 j= 89349\nElapsed duration:  0 seconds\n"}︡{"stdout":"g^x =  387420489 = A =  387420489 ( True )\n"}︡{"done":true}
︠055e39e5-df7c-474e-8df5-1293ccfd0671s︠
# Testing object pointers and list/set
a = [1,2,3]
id(a)
︡4f9e25c9-380c-48d2-902e-fea18d4ec3aa︡{"stdout":"140224805362720\n"}︡{"done":true}
︠8f639e15-0558-455c-bba9-e0608e276a4bs︠
b = set(a)
id(b)
︡736f857c-45e4-40ad-98de-34ef03b48d41︡{"stdout":"140224805641472\n"}︡{"done":true}
︠39e1b339-44ad-4fe9-8e8f-223feeedf04es︠
id(a)
︡2f4102b6-de3e-4a7a-95cf-4a327d9f753d︡{"stdout":"140224805362720\n"}︡{"done":true}
︠ce0e4362-3276-4c10-b680-499f504fb673︠









