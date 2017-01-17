I tested the various root finding methods with three functions. 
###First function
$f(x) = x^3 - x^2 $

This function generates roots at x = 0,1. Bisection methods and Brent's methods work really well with this function, if the boundaries are chosen properly. However, the Newton method has a lot of trouble finding the roots. I think it is because this particular function has a couple tight oscillations near the roots, as the cubed power takes over the square. This causes the Newton method to overshoot.

###Second Function
$f(x) = sin(10x)e^{-x}$

This function also works well with Bisection/Brent methods, but fails with Newton. The function has many oscillations, so it is easy for the Newton method to overshoot. I checked the Newton method with a value near a root found by Bisection, and the Newton method did not converge. 

###Third Function
$f(x) = 8e^x - 5e^{x^2}$

This function actually worked well for everything, as it has only a few roots and no oscillatory shape. 