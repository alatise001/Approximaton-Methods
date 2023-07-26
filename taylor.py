from sympy import diff, symbols, factorial, pretty_print, sin, cos, tan, pi, exp

x = symbols("x")

func = eval(input("Enter Function______"))
a0 = int(input("Enter Known Point ______"))
n = eval(input("Enter Number of Iteration ______"))
val = int(input("Enter Error Point____"))


def taylor_series(func, a0, n, x):
    result = func.subs(x, a0)

    for i in range(1, n):
        result += diff(func, x, i).subs(x, a0) * (x - a0) ** i / factorial(i)

        error = (func.subs(x, val) - result.subs(x, val)) / func.subs(x, val)

        print("Error: ", float(error))

    pretty_print(result)


taylor_series(func, a0, n, x)

# taylor series of sin cos tan  with
