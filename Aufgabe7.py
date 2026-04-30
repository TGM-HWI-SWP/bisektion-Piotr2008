import math
import matplotlib.pyplot as plt


def f(x: float, funktion: str) -> float:
    """Berechnet den Funktionswert."""
    # eval() berechnet die Funktion, die als Text eingegeben wurde.
    return float(eval(funktion, {"__builtins__": {}}, {"x": x, "math": math}))


def bisektion_verlauf(
    funktion: str,
    a: float,
    b: float
) -> tuple[list[int], list[float], list[float]]:
    """Speichert die Werte der Bisektionsmethode für die Animation."""

    iterationen = []
    x_werte = []
    genauigkeiten = []

    # Maximal 30 Schritte, damit die Animation sicher irgendwann aufhört.
    for i in range(30):
        # Mittelpunkt des Intervalls berechnen
        c = (a + b) / 2

        # Funktionswert am Mittelpunkt berechnen
        fc = f(c, funktion)

        # Werte für die Diagramme speichern
        iterationen.append(i + 1)
        x_werte.append(c)
        genauigkeiten.append(abs(fc))

        # Wenn f(c) nahe genug bei 0 ist, wird abgebrochen.
        if abs(fc) < 1e-7:
            break

        # Prüfen, in welcher Intervallhälfte die Nullstelle liegt
        if f(a, funktion) * fc < 0:
            b = c
        else:
            a = c

    return iterationen, x_werte, genauigkeiten


def zeichne_animation(funktion: str, a: float, b: float) -> None:
    """Zeichnet eine einfache Animation mit zwei Diagrammen."""

    # Berechnung der Werte für die Animation
    iterationen, x_werte, genauigkeiten = bisektion_verlauf(funktion, a, b)

    # Zwei Diagramme untereinander erstellen
    fig, axes = plt.subplots(2, 1, figsize=(8, 7))

    # Schrittweise Darstellung der gespeicherten Werte
    for i in range(len(iterationen)):
        # Alte Zeichnung löschen, damit ein neuer Animationsschritt entsteht
        axes[0].clear()
        axes[1].clear()

        # Diagramm 1: Genauigkeit
        axes[0].plot(iterationen[:i + 1], genauigkeiten[:i + 1], marker="o")
        axes[0].set_title("Genauigkeit je Iteration")
        axes[0].set_xlabel("Iteration")
        axes[0].set_ylabel("|f(x)|")
        axes[0].grid(True)

        # Diagramm 2: aktuelle Lösung x
        axes[1].plot(iterationen[:i + 1], x_werte[:i + 1], marker="o")
        axes[1].set_title("Aktuelle Lösung x")
        axes[1].set_xlabel("Iteration")
        axes[1].set_ylabel("x")
        axes[1].grid(True)

        # Layout anpassen und kurz pausieren
        plt.tight_layout()
        plt.pause(0.4)

    # Fenster offen lassen, nachdem die Animation fertig ist
    plt.show()


def main() -> None:
    """Startet Aufgabe 7."""
    print("Aufgabe 7: einfache Animation")
    print("Beispiel: x**2 - 25")

    try:
        funktion = input("Funktion: ")
        a = float(input("Startwert a: "))
        b = float(input("Endwert b: "))

        # Vorzeichenwechsel prüfen
        if f(a, funktion) * f(b, funktion) >= 0:
            print("Fehler: Kein Vorzeichenwechsel im Intervall.")
            return

        # Animation starten
        zeichne_animation(funktion, a, b)

    except ValueError:
        print("Fehler: Bitte gültige Zahlen eingeben.")


if __name__ == "__main__":
    main()