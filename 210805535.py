print("Welcome!----")


inputList = [2, -5, -2, 1, 2]


def main(inputList):
    def secant_method(inputList):
        a = int(inputList[0])
        b = int(inputList[1])
        c = int(inputList[2])

        s = int(inputList[3])
        r = int(inputList[4])

        def f(g):
            f = a * g**3 + b * g + c
            return f

        for itercept in range(1, 5):
            fs = f(s)
            fr = f(r)

            xi = s - fs / ((fs - fr) / (s - r))

            s = r
            r = xi

        print(f"{round(xi, 6)} for Secant Method")

    def newtons_method(inputList):
        a = int(inputList[0])
        b = int(inputList[1])
        c = int(inputList[2])

        s = int(inputList[3])

        def f(g):
            f = a * g**3 + b * g + c
            return f

        def df(g):
            df = 3 * a * g**2 + b
            return df

        for itercept in range(1, 5):
            l = s - (f(s) / df(s))
            s = l

        print(f"{round(s, 6)} for Newton Method")

    def bisection_method(inputList):
        a = int(inputList[0])
        b = int(inputList[1])
        c = int(inputList[2])

        s = int(inputList[3])
        r = int(inputList[4])

        def f(g):
            f = a * g**3 + b * g + c
            return f

        errorValue = abs(r - s)

        for l in range(0, 5):
            e = (r + s) / 2

            if f(s) * f(r) >= 0:
                print(
                    "No root or multiple roots present, bisection select will not work"
                )
                quit()

            elif f(e) * f(s) < 0:
                r = e
                errorValue = abs(r - s)

            elif f(e) * f(r) < 0:
                s = e
                errorValue = abs(r - s)

            else:
                print("something went wrong")
                quit()

        print(f"{round(f(e), 6)} for Bisection Method")

    if len(inputList) != 5:
        newtons_method(inputList)
    else:
        bisection_method(inputList)
        secant_method(inputList)


main(inputList)
