import random

print("Welcome!----")


figure = [4, 3, -3, 0, 1]


def main(figure):
    def bisection_method(figure):
        a = int(figure[0])
        b = int(figure[1])
        c = int(figure[2])

        s = int(figure[3])
        r = int(figure[4])

        def f(x):
            f = a * x**3 + b * x + c
            return f

        error = abs(r - s)

        for i in range(0, 5):
            d = (r + s) / 2

            if f(s) * f(r) >= 0:
                print(
                    "No root or multiple roots present, bisection select will not work"
                )
                quit()

            elif f(d) * f(s) < 0:
                r = d
                error = abs(r - s)

            elif f(d) * f(r) < 0:
                s = d
                error = abs(r - s)

            else:
                print("something went wrong")
                quit()

        print(
            f"For Bisection Method The root was found to be at {round(f(d), 6)} after {5} iterations"
        )
        print(f"For Bisection Method The error is {round(error, 6)}")
        print(f"The lower boundary a is {s} and the upper boundary, b is {r}\n")

    def newtons_method(figure):
        a = int(figure[0])
        b = int(figure[1])
        c = int(figure[2])

        s = int(figure[3])

        def f(x):
            f = a * x**3 + b * x + c
            return f

        def df(x):
            df = 3 * a * x**2 + b
            return df

        for itercept in range(1, 5):
            i = s - (f(s) / df(s))
            s = i

        print(
            f"For Newton Method\nThe root was found to be at {round(s, 6)} after {10} iterations\n"
        )

    def secant_method(figure):
        a = int(figure[0])
        b = int(figure[1])
        c = int(figure[2])

        s = int(figure[3])
        r = int(figure[4])

        def f(x):
            f = a * x**3 + b * x + c
            return f

        for itercept in range(1, 5):
            fs = f(s)
            fr = f(r)

            xi = s - fs / ((fs - fr) / (s - r))

            s = r
            r = xi

        print(
            f"For Secant Method\nThe root was found to be at {round(xi, 6)} after {5} iterations!\n"
        )

    if len(figure) != 5:
        newtons_method(figure)
    else:
        hint = random.choice([0, 1])

        if hint == 0:
            return bisection_method(figure)
        else:
            return secant_method(figure)


main(figure)
