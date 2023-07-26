func = input("Enter Function______")
x0 = int(input("Enter Lower Root Boundary______"))
x1 = int(input("Enter Upper Root Boundary______"))
tolerance = eval(input("Enter Tolerance______"))


def secant_method(func, x0, x1, n):
    def f(x):
        f = eval(func)
        return f

    for itercept in range(1, n):
        fx0 = f(x0)
        fx1 = f(x1)

        xi = x0 = fx0 / ((fx0 - fx1) / (x0 - x1))

        x0 = x1
        x1 = xi

    print(f"The root was found to be at {x} after {n}iterations!")


secant_method(func, x0, x1, tolerance)
