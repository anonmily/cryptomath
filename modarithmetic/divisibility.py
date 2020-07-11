import math

def xgcd(a,b,):
    # Extended Euclidean Algorithm
    # From: http://anh.cs.luc.edu/331/notes/xgcd.pdf
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = math.floor(a/b)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    #print(f'd={a}, x={prevx}, y={prevy}')
    return (int(a), int(prevx), int(prevy))