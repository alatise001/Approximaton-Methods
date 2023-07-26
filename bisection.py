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
            print("No root or multiple roots present, bisection method will not work")
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
