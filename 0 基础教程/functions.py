def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

import math
def quadratic(a,b,c):
    d = b**2-4*a*c

    if d == 0:
        x = (-b-d)/(2*a)
        return x
    elif d>0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return x1,x2

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5,2)