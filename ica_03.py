import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import question2 as q2

def f1(x):
    return x**3.0 - x**2.0

def f2(x):
    return np.sin(10*x)*np.exp(-x)

def f3(x):
    return 8*np.exp(-x) - 5*np.exp(x**2.0)


#q2.bisect(0.5,1.5,f2,1000.0,1e-4)
q2.newt(1.2,f2,1000,1e-4)
#op.brent(f2,0.0,0.5)
