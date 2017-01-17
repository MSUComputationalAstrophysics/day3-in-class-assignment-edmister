import numpy as np
from scipy.misc import derivative

# bisection algorithm for finding roots
# INPUTS:
#       a    - lower bound x value
#       b    - upper bound x value
#       f    - input function
#       nmax - max iteration number
#       emin - min function value for declaring root
def bisect(a,b,f,nmax,emin):
    print("Entering bisection method.")
    print("emin = ",emin,' nmax = ',nmax)
    n = 0
    e = 2.0*emin
    while n<nmax:
        c = 0.5*(a + b)
        e = (b - a)/2.0
        if (np.sign(f(a)) == np.sign(f(c))):
            a = c
        else:
            b = c

        n += 1
        print('n = ',n)
        print('e = ',e)
        print('x = ',c)
        print('f(x) = ',f(c))
        if e < emin:
            break


    return

# Newton algorithm for root finding
# INPUTS:
#       x    - initial guess
#       f    - input Function
#       nmax - max number of iterations
#       emin - min fuction value threshold
def newt(x,f,nmax,emin):
    print("Entering Newton method. ")
    n = 0
    e = 2*emin
    while n < nmax:
        d = derivative(f,x)
        e = f(x)/d
        x = x - e
        n += 1
        print("=================")
        print('n = ',n)
        print("x = ",x)
        print("f(x) = ",f(x))
        print("f'(x) = ",d)
        if e < emin:
            break
    return
