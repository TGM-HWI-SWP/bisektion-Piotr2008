import math

def solver():
    print("Aufgabe 5: Bisektion")
    print("Beispiel: x**2 - 25")

    funktion = input("Funktion: ")
    a = float(input("a: "))
    b = float(input("b: "))

    ergebnis = bisektion(funktion, a, b)

    if ergebnis:
        x, it = ergebnis
        print(f"Nullstelle: {x}")
        print(f"f(x) = {f(x, funktion)}")
        print(f"Iterationen: {it}")


def f(x: float, funktion: str) -> float:
    try:
        return float(eval(funktion, {"__builtins__": {}}, {"x": x, "math": math}))
    except Exception as error:
        raise ValueError(f"Fehler: {error}")


def bisektion(funktion: str, a: float, b: float, tol: float = 1e-7, max_iter: int = 100):
    if f(a, funktion) * f(b, funktion) >= 0:
        print("Kein Vorzeichenwechsel!")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c, funktion)) < tol:
            return c, i + 1

        if f(a, funktion) * f(c, funktion) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, max_iter
if __name__ == "__main__":
    
    solver()

