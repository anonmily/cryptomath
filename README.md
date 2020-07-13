# Cryptography Math Tools

This is an assortment of code written while learning cryptography.
Things are more than likely to change frequently as I learn new things.
Feel free to provide suggestions or improvements.

This code uses Python 3.8.2.

# Running Sage Locally
If you don't have sage installed locally already, you can also run it via [Docker](https://www.docker.com/get-started). This repository includes a [Docker Compose](https://docs.docker.com/compose/gettingstarted/) file that can be used and adapted.

```
version: '3'
services:
  sage:
    image: sagemath/sagemath:latest
    ports:
     - "8888:8888"
    volumes:
      - .:/src
    working_dir: /src
```

To start up a container bash terminal, just run
```
docker-compose run sage bash
```
This will open a bash terminal in the container with this current directory mounted to /src, which is the working directory.

Then, you can run `sage --python` followed by your filename to run a python file with sage.
```python
# experiment.py
# sage libraries can now be imported and used

from sage.all import *
print(factor(1000))
```

```bash
sage --python experiment.py
```

```bash
sage@56b9c372c099:/src$ ls
README.md  discrete_log_problem  docker-compose.yml  experiment.py  matrices.py  modarithmetic  utils.py

sage@56b9c372c099:/src$ sage --python experiment.py
2^3 * 5^3
```


# Modular Arithmetic

## Extended Euclidean Algorithm:
```python
from modarithmetic import xgcd
# Returns a tuple: (38, 32, -45)
# d=38, x=32, y=-45
d, x, y = xgcd(4864, 3458) 
```

## Find a x such that f(x) is congruent to c mod m
![f(x) = c mod m](https://latex.codecogs.com/svg.latex?f(x)\equiv%20c%20\mod%20m)
```python
from modarithmetic import find_x_for_mod

# f(x) = 5x
f = lambda x: 5*x 

x = find_x_for_mod(f, c=4, m=3)
```
## Find discrete root for x^2 congruent to c mod p
If  ![p-mod-4-congruent-3](https://latex.codecogs.com/svg.latex?p%20\equiv%203%20\mod%204)   then the discrete root is:  
![discrete-root-for-p-mod-4-congruent-3](https://latex.codecogs.com/svg.latex?x=\pm%20c^{\frac{p+1}{4}}\mod%20p)

Otherwise, use the brute-force find_x_for_mod to find the discrete root.
```python
from modarithmetic import get_discrete_root

x1, x2 = get_discrete_root(2201, 4127)
```

## Find the composite discrete root for x^2 congruent to c mod m
If the moduli m is composite and can be reduced to prime power modules...
1. Prime factorization of m:  

![factor-m](https://latex.codecogs.com/svg.latex?m=p_1^{a_1}%20\cdots%20p_k^{a_k})

2. Compute the square root modulo each of the the prime
3. Combine using the Chinese Remainder Theorem

```python
from modarithmetic import get_composite_discrete_root

# Will return [144, 201, 236, 293]
roots = get_composite_discrete_root(197, 437)
```

## Get modular inverse
![equation](https://latex.codecogs.com/svg.latex?a%20\bullet%20a^{-1}%20%20\equiv%201%20(mod%20m))
```python
from modarithmetic import get_mod_inverse
a_inv = get_mod_inverse(a=2, m=7)
```

## Chinese Remainder Problem
* Solves a system of congruences for the general solution of x.
* Returns the final c and final m for the generalized solution x as a tuple (c, m)

![x=c+mk](https://latex.codecogs.com/svg.latex?x=c%20+%20mk)

* Should work for any number of equations now.

![x=c (mod m)](https://latex.codecogs.com/svg.latex?x%20\equiv%20c%20\mod%20m)

For example:

![x=3 (mod 7)](https://latex.codecogs.com/svg.latex?x%20\equiv%203%20\mod%207)

![x=9 (mod 13)](https://latex.codecogs.com/svg.latex?x%20\equiv%209%20\mod%2013)

```python
from modarithmetic import chinese_remainder_theorem

# Represent the equations in pairs of (c,m)
c, m = chinese_remainder_theorem([ 
    (3,7), 
    (9,13) 
])
general_x = lambda k: c + m*k

# 4 equations
c, m = chinese_remainder_theorem([
    (1,3), (1,4), 
    (1,5), (0,7)
])
general_x = lambda k: c + m*k
```

# Discrete Log Problem
## Baby Step Giant Step Algorithm
```python
p = 200003000003
g = 3
A = 387420489

x = babygiantstep( p, g, A )

assert( pow(g, x, p) == A )
```
## Pohlig Hellman Algorithm
* Currently only applicable to Fp
* Reduces the discrete log problem (DLP) of elements of arbitary order and reduces it to the DLP of prime power order.

For example:
![g=15,h=131,p=337](https://latex.codecogs.com/svg.latex?15^{x}%20\equiv%20131%20\mod%20337)

```python
from discrete_log_problem import pohlig_hellman

pohlig_hellman(g=15, h=131, p=337)
```

Terminal Output:
```
n= 336
n_factors= 2^4 * 3 * 7
--------------------
p0=16
exp0=21
g0=4987885095119476318359375
h0=290199866805246507499041077857400346603111731
y0=60
x0=60 (mod 16)
--------------------
p1=3
exp1=112
g1=527498239136944143011835266282070782918534060023346029923092533291348073833388315816706457851703593320280560874380171298980712890625
h1=1362652487794305072533342841626523269381517362311183922718660677237200246515771042225328028259800909540500683767373213278113598345531550833789248253352735012508378740470544110793410298513818508835741654961778574600025940702716062123104961
y1=20
x1=20 (mod 3)
--------------------
p2=7
exp2=48
g2=283387333428466483068181247517713927663862705230712890625
h2=425620160816387295235804131795702204210010991404753276397921099580173916714524850438751065515767381441
y2=19
x2=19 (mod 7)
--------------------
x= 236
```