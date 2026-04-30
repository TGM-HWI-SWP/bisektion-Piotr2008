import math


def f(x: float, funktion: str) -> float:
    return float(eval(funktion, {"__builtins__": {}}, {"x": x, "math": math}))


def bisektion(funktion: str, a: float, b: float, tol: float):
    for i in range(100):
        c = (a + b) / 2
        if abs(f(c, funktion)) < tol:
            return c, i + 1

        if f(a, funktion) * f(c, funktion) < 0:
            b = c
        else:
            a = c

    return c, i + 1


def main():
    print("Aufgabe 8")

    funktion = "2*x + x**2 + 3*x**3 - x**4"
    a, b = 3, 4

    x1, it1 = bisektion(funktion, a, b, 1e-2)
    print("\nε = 1e-2")
    print(f"x = {x1}, Iterationen = {it1}")

    x2, it2 = bisektion(funktion, a, b, 1e-8)
    print("\nε = 1e-8")
    print(f"x = {x2}, Iterationen = {it2}")


if __name__ == "__main__":
    main()