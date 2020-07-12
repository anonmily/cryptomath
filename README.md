# Cryptography Math Tools

This is an assortment of code written while learning cryptography.
Things are more than likely to change frequently as I learn new things.
Feel free to provide suggestions or improvements.

This code uses Python 3.8.2.

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

## Get modular inverse
![equation](https://latex.codecogs.com/svg.latex?a%20\bullet%20a^{-1}%20%20\equiv%201%20(mod%20m))
```python
from modarithmetic import get_mod_inverse
a_inv = get_mod_inverse(a=2, m=7)
```

## Chinese Remainder Problem
* Solves a system of congruences for the general solution of x.
* Returns a lambda function for the general solution (e.g. lambda t: 87 + 91*t)
* Currently works only for a system of two congruences.

![x=c (mod m)](https://latex.codecogs.com/svg.latex?x%20\equiv%20c%20\mod%20m)

For example:

![x=3 (mod 7)](https://latex.codecogs.com/svg.latex?x%20\equiv%203%20\mod%207)

![x=9 (mod 13)](https://latex.codecogs.com/svg.latex?x%20\equiv%209%20\mod%2013)

```python
from modarithmetic import chinese_remainder_theorem

# Represent the equations in pairs of (c,m)
sys_of_congruences = [(3,7), (9,13)]

chinese_remainder_theorem(sys_of_congruences)
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
