print("Welcome!----")


method = input(
    "Please Select a Non-Linear Method, enter\nA for Bisection Method,\nB for Newtons,\nC for Secant,\nD for Taylor Method,\nE for Euler,\nF for Picard_____"
)


if method.upper() == "A":
    func = input("Enter Function______")
    a = int(input("Enter Lower Root Boundary______"))
    b = int(input("Enter Upper Root Boundary______"))
    tolerance = eval(input("Enter Tolerance______"))

    def bisection_method(func, a, b, tolerance):
        def f(x):
            f = eval(func)
            return f

        error = abs(b - a)

        while error > tolerance:
            c = (b + a) / 2

            if f(a) * f(b) >= 0:
                print(
                    "No root or multiple roots present, bisection method will not work"
                )
                quit()

            elif f(c) * f(a) < 0:
                b = c
                error = abs(b - a)

            elif f(c) * f(b) < 0:
                a = c
                error = abs(b - a)

            else:
                print("something went wrong")
                quit()

        print(f"The error is {error}")
        print(f"The lower boundary a is {a} and the upper boundary, b is {b}")

    bisection_method(func, a, b, tolerance)

elif method.upper() == "B":
    func = input("Enter Function______")
    dirivedfunc = input("Enter Dirived Function______")
    x = eval(input("Enter Root Boundary______"))
    n = int(input("Enter Tolerance______"))

    def newtons_method(func, dirivedfunc, x, n):
        def f(x):
            f = eval(func)
            return f

        def df(x):
            df = eval(dirivedfunc)
            return df

        for itercept in range(1, n):
            i = x - (f(x) / df(x))
            x = i

        print(f"The root was found to be at {x} after {n} iterations")

    newtons_method(func, dirivedfunc, x, n)


elif method.upper() == "C":
    func = input("Enter Function______")
    x0 = int(input("Enter Lower Root Boundary______"))
    x1 = int(input("Enter Upper Root Boundary______"))
    tolerance = eval(input("Enter Tolerance/Iteration ______"))

    def secant_method(func, x0, x1, n):
        def f(x):
            f = eval(func)
            return f

        for itercept in range(1, n):
            fx0 = f(x0)
            fx1 = f(x1)

            xi = x0 - fx0 / ((fx0 - fx1) / (x0 - x1))

            x0 = x1
            x1 = xi

        print(f"The root was found to be at {xi} after {n} iterations!")

    secant_method(func, x0, x1, tolerance)


elif method.upper() == "D":
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


elif method.upper() == "E":
    import math

    x0 = float(input("Enter Intial Conditon of x0 ______"))
    y0 = float(input("Enter Intial Conditon of y0 ______"))
    h = float(input("Enter the Value of h____"))
    n = int(input("Enter The Number Of Iteration n____"))

    def euler_method(x0, y0, h, n):
        def f(x, y):
            return x + y

        def f_exact(x):
            return -x - 1 + math.exp(x)

        for i in range(n):
            y1 = y0 + h * f(x0, y0)
            x0 = x0 + h
            y0 = y1

            print(f"Value of y at x", round(x0, 2), "is = ", round(y0, 3))
        print("Exact =", f_exact(1))

        err = abs(f_exact(x0) - y0)

        print("Error =", err)

    euler_method(x0, y0, h, n)

else:
    print("Invalid Input")
