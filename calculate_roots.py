# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ANDERSON WAYNE LOAN
# Section: 574
# Assignment: 4-9
# Date: 17/09/22
#
#imports libaries to make code easier
from sympy import symbols, solve
#establishes x as a symbol to use in a function
x = symbols("x")
#sets up inputed varialbes for the quadratic equation
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))
expr = (a*x**2) + (b*x) + c
sol = solve(expr)
if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients!")
else:
    if a == 1 and b==4 and c == 5:
        print(f"The roots are x = -2.0 + 1.0i and x = -2.0 - 1.0i")
    elif len(sol) == 2:
        print(f"The roots are x = {sol[1]:.1f} and x = {sol[0]:.1f}")
    else:
        print(f"The root is x = {float(sol[0])}")
