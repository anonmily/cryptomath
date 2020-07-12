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

x = find_x_for_mod(f, c=4, m=3, print_all=True)
```
## Find discrete root for x^2 congruent to c mod p
If  ![p-mod-4-congruent-3](https://latex.codecogs.com/svg.latex?p%20\equiv%203%20\mod%204)   then the discrete root is:  
![discrete-root-for-p-mod-4-congruent-3](https://latex.codecogs.com/svg.latex?x=\pm%20c^{\frac{p+1}{4}}\mod%20p)

Otherwise, use the brute-force find_x_for_mod to find the discrete root.

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
