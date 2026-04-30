import math


def f(x: float, funktion: str) -> float:
    return float(eval(funktion, {"__builtins__": {}}, {"x": x, "math": math}))


def bisektion(funktion: str, a: float, b: float):
    for i in range(100):
        c = (a + b) / 2
        if abs(f(c, funktion)) < 1e-8:
            return c, i + 1

        if f(a, funktion) * f(c, funktion) < 0:
            b = c
        else:
            a = c

    return c, i + 1


def main():
    print("Aufgabe 9")

    funktion = "x * math.cosh(50 / x) - x - 10"

    a, b = 100, 200

    radius, it = bisektion(funktion, a, b)

    laenge = 2 * radius * math.sinh(100 / (2 * radius))

    print(f"Krümmungsradius a: {radius}")
    print(f"Iterationen: {it}")
    print(f"Länge: {round(laenge, 2)} m")


if __name__ == "__main__":
    main()