import math

def solver2():
    """
    Hauptprogramm für Aufgabe 6.
    Hier kann der Benutzer entweder eigene Werte eingeben
    oder die vorbereiteten Tests ausführen.
    """
    print("Aufgabe 6: Nullstellenberechnung mit Regula falsi")
    print("1 = eigene Funktion eingeben")
    print("2 = Tests mit n = 25, 81 und 144")

    try:
        auswahl = input("Wähle 1 oder 2: ")

        if auswahl == "1":
            # Beispiele helfen dem Benutzer bei der richtigen Eingabe.
            print("\nBeispiele für Funktionen:")
            print("Wurzel aus 25: x**2 - 25")
            print("Polynom: 2*x + x**2 + 3*x**3 - x**4")
            print("Mit Sinus: math.sin(x)")
            print("Mit Kosinus: math.cos(x) - x")

            funktion = input("\nGib jetzt die ganze Funktion mit x ein: ")
            a = float(input("Gib den Startwert a ein: "))
            b = float(input("Gib den Endwert b ein: "))

            # Aufruf der Regula-falsi-Methode.
            loesung = regula_falsi(funktion, a, b)

            # Ausgabe des Ergebnisses, falls eine Lösung gefunden wurde.
            if loesung is not None:
                print("\nErgebnis:")
                print(f"Gefundene Nullstelle: {loesung}")
                print(f"f({loesung}) = {f(loesung, funktion)}")

        elif auswahl == "2":
            # Führt die vorbereiteten Testfälle aus.
            teste_wurzelwerte()

        else:
            print("Fehler: Bitte 1 oder 2 eingeben.")

    except ValueError:
        # Fehlerbehandlung, falls a oder b keine Zahlen sind.
        print("Fehler: Bitte gültige Zahlen eingeben.")  


    if __name__ == "__main__":
    
        solver2()

def f(x: float, funktion: str) -> float:
    """
    Berechnet den Funktionswert einer eingegebenen Funktion.
     Beispiel:
    x = 5
    funktion = "x**2 - 25"
    Ergebnis: 0
    """
    try:
        # eval() berechnet die Funktion, die als Text eingegeben wurde.
        # x wird dabei durch den aktuellen Zahlenwert ersetzt.
        return float(eval(funktion, {"__builtins__": {}}, {"x": x, "math": math}))

    except Exception as error:
        # Falls die Funktion falsch eingegeben wurde,
        # wird eine verständliche Fehlermeldung erzeugt.
        raise ValueError(f"Fehler in der Funktion: {error}")


def regula_falsi(
    funktion: str,
    a: float,
    b: float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> float | None:
    """
    Berechnet eine Nullstelle mit der Regula-falsi-Methode.

    funktion: Funktion als Text, z.B. "x**2 - 25"
    a: linker Startwert des Intervalls
    b: rechter Startwert des Intervalls
    tol: gewünschte Genauigkeit
    max_iter: maximale Anzahl an Iterationen
    """
    try:
        # Zuerst wird geprüft, ob zwischen a und b ein Vorzeichenwechsel liegt.
        # Ohne Vorzeichenwechsel kann die Methode keine sichere Nullstelle finden.
        if f(a, funktion) * f(b, funktion) >= 0:
            print("Fehler: Kein Vorzeichenwechsel im Intervall [a, b].")
            return None

        # Startwert für c, damit c später sicher existiert.
        c = a

        # Die Schleife wiederholt das Verfahren maximal max_iter-mal.
        for i in range(max_iter):
            # Funktionswerte an den Intervallgrenzen berechnen.
            fa = f(a, funktion)
            fb = f(b, funktion)

            # Regula-falsi-Formel:
            # c ist der Schnittpunkt der Sekante mit der x-Achse.
            c = (a * fb - b * fa) / (fb - fa)

            # Funktionswert an der neuen Stelle c berechnen.
            fc = f(c, funktion)

            # Aktuellen Iterationsschritt ausgeben.
            print(f"Iteration {i + 1}: x = {c}, f(x) = {fc}")

            # Wenn f(c) nahe genug bei 0 liegt,
            # wurde die Nullstelle genau genug gefunden.
            if abs(fc) < tol:
                return c

            # Nun wird entschieden, welche Intervallseite ersetzt wird.
            # Die Nullstelle liegt immer dort, wo ein Vorzeichenwechsel ist.
            if fa * fc < 0:
                b = c
            else:
                a = c

        # Falls die maximale Iterationszahl erreicht wurde,
        # wird die letzte Näherung zurückgegeben.
        return c

    except ValueError as error:
        print(error)
        return None


def teste_wurzelwerte() -> None:
    """
    Testet die Regula-falsi-Methode mit n = 25, 81 und 144.

    Für die Wurzel wird die Gleichung x**2 = n umgeformt zu:
    x**2 - n = 0
    """
    zahlen = [25, 81, 144]

    for n in zahlen:
        # Für jede Zahl wird eine passende Funktion erstellt.
        funktion = f"x**2 - {n}"

        print(f"\nTest für n = {n}")

        # Regula falsi berechnet die numerische Näherung.
        loesung = regula_falsi(funktion, 0, n)

        # math.sqrt(n) ist die analytische Vergleichslösung.
        analytisch = math.sqrt(n)

        print(f"Numerische Lösung: {loesung}")
        print(f"Analytische Lösung: {analytisch}")



if __name__ == "__main__":

    solver2()