from sympy import symbols, diff, cos, sin, tan, pretty_print

x, y = symbols("x y")

exp1 = 2 * x + 5

exp2 = x**3

exp3 = cos(x)


print(diff(exp3, x))
