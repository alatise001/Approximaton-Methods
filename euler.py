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
