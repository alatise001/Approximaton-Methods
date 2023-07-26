func = input("Enter Function______")
dirivedfunc = input("Enter Dirived Function______")
x = int(input("Enter Root Boundary______"))
n = int(input("Enter Tolerance______"))


def newtons_method(func, dirivedfunc, x, n):
    def f(x):
        f = eval(func)
        return f

    def df(x):
        f = eval(funcderiv)
        return df

    for itercept in range(1, n):
        i = x - (f(x) / df(x))
        x = i

    print(f"The root was found to be at {x} after {n}iterations")


newtonsmethod(func, dirivedfunc, x, n)
