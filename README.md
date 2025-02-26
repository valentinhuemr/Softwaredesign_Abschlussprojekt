# Softwaredesign_Abschlussprojekt
1. Einleitung
Das Ziel dieses Projekts ist die Simulation eines Mechanismus mit beweglichen Gelenken und Stäben. Die Simulation ermöglicht die Berechnung von Gelenkpositionen, Längenoptimierungen und die Visualisierung der Mechanik in einer grafischen Oberfläche (GUI). Zudem besteht die Möglichkeit, Mechanismen zu speichern und später erneut zu laden.
2. Projektstruktur
Das Projekt besteht aus vier Hauptmodulen:
•	Mechanism: Implementierung des Mechanismus mit Gelenken, Stäben und Bewegungssimulationen.
•	Simulation: Berechnung der Bewegung des Mechanismus und optionale Speicherung als GIF.
•	Storage: Speichern und Laden von Mechanismen aus einer Datenbank oder einem Dateisystem.
•	GUI: Eine grafische Benutzeroberfläche zur Interaktion mit der Simulation.
3. Klassendiagramm
![UML-Diagramm](Images/UML-Diagramm.png)
4. Funktionsweise
Das Programm funktioniert folgendermaßen:
1.	Der Nutzer erstellt einen neuen Mechanismus in der GUI.
2.	Die Mechanism-Klasse berechnet die Positionen der Gelenke und die optimalen Stablängen.
3.	Die Simulation-Klasse simuliert die Bewegung des Mechanismus und kann diese als GIF speichern.
4.	Der Mechanismus kann durch die Storage-Klasse gespeichert oder geladen werden.
