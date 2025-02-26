# Softwaredesign_Abschlussprojekt

## 1. Einleitung
Das Ziel dieses Projekts ist die Simulation eines Mechanismus mit beweglichen Gelenken und Stäben. Die Simulation ermöglicht:

- Berechnung der Gelenkpositionen
- Längenoptimierungen
- Visualisierung der Mechanik in einer grafischen Oberfläche (GUI)

Zusätzlich besteht die Möglichkeit, Mechanismen zu speichern und später erneut zu laden.

## 2. Projektstruktur
Das Projekt besteht aus vier Hauptmodulen, die jeweils eine bestimmte Funktionalität abdecken:

### - **Mechanism**
  - Implementierung des Mechanismus mit Gelenken, Stäben und Bewegungssimulationen.

### - **Simulation**
  - Berechnung der Bewegung des Mechanismus.
  - Optionale Speicherung der Simulation als GIF.

### - **Storage**
  - Speichern und Laden von Mechanismen aus einer Datenbank oder einem Dateisystem.

### - **GUI**
  - Eine grafische Benutzeroberfläche zur Interaktion mit der Simulation.

## 3. Klassendiagramm
Hier ist das UML-Diagramm, das die Architektur und die Beziehungen zwischen den Klassen visualisiert:

![UML-Diagramm](Images/UML-Diagramm.png)

## 4. Funktionsweise
Das Programm funktioniert folgendermaßen:

1. **Neuen Mechanismus erstellen**: Der Nutzer erstellt einen neuen Mechanismus in der GUI.
2. **Berechnung der Gelenkpositionen**: Die `Mechanism`-Klasse berechnet die Positionen der Gelenke und die optimalen Stablängen.
3. **Simulation der Bewegung**: Die `Simulation`-Klasse simuliert die Bewegung des Mechanismus und kann diese als GIF speichern.
4. **Speichern und Laden**: Der Mechanismus kann durch die `Storage`-Klasse gespeichert oder geladen werden.

