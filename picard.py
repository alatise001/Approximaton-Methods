from sympy import symbols, pretty_print, sin, cos, tan, pi, exp, integrate

x = symbols("x")
y = symbols("y")

func = eval(input("Enter Function______"))
y0 = int(input("Enter y0 ______"))
x0 = int(input("Enter x0 ______"))
n = eval(input("Enter Number of Iteration ______"))


def picard_method(func, y0, x0, n, x, y):
    result = y0

    for i in range(1, n):
        result += integrate(func, x0, x, args=(y)).subs(y, y0) + y0
        y0 = y1

        # error = (func.subs(x, val) - result.subs(x, val)) / func.subs(x, val)
        # print("Error: ", float(error))

    pretty_print(result)


picard_method(func, y0, x0, n, x, y)
