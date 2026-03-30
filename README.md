## Warum ich das gebaut habe

Ich habe das Projekt hauptsächlich gebaut, um Pandas besser zu verstehen.

Ich hatte das Gefühl, dass ich zwar pandas Code schreiben kann, aber nicht wirklich verstehe, was mit den Daten im Hintergrund passiert. Deshalb wollte ich etwas Eigenes bauen, wo ich gezwungen bin, mich damit auseinanderzusetzen.

⸻

Was schwierig war

Am meisten hat mich groupby() beschäftigt.

Nicht unbedingt die fuktion selbst, sondern zu verstehen was für ein Objekt daraus entsteht:
	•	Wann ist es noch ein DataFrame?
	•	Wann wird es eine Series?

Ich musste öfter stoppen und mir die Daten angucken, um nicht komplett den Überblick zu verlieren.

⸻

Was gut funktioniert hat

Eine Sache, die überraschend gut funktioniert hat waren kleine Funktionen.

Am Anfang war ich eher versucht, größere Logikblöcke zu bauen. Das wurde schnell unübersichtlich.
Erst als ich angefangen habe, alles in kleine Schritte zu zerlegen, wurde es kontrollierbar.

⸻

Was ich heute anders machen würde

Die UI ist nicht gut strukturiert:
Der Upload ist aktuell in der Mitte und vermischt sich mit dem Report.
Ich würde das klar trennen, wahrscheinlich über eine Sidebar damit der Nutzer besser versteht was Input und was Output ist.

⸻

Für wen das gedacht ist

Für Leute, die Verkaufsdaten auswerten wollen, ohne alles manuell zu machen.

Ist kein fertiges Produkt, eher ein Werkzeug oder Ausgangspunkt.

⸻

Ehrliche Schwächen
	•	Die Spaltennamen müssen ziemlich genau passen
	•	Wenig flexibel bei unterschiedlichen Datensätzen
	•	UI ist eher funktional als durchdacht

Ich habe versucht, die Spalten zu bereinigen, aber am Ende hängt es immer noch an bestimmten Begriffen.

⸻

Was ich daraus mitgenommen habe
	•	Zu komplizierte Lösungen machen alles nur schwerer
	•	Kleine Schritte/Funktionen sind langsamer am Anfang, aber sparen viel Zeit später

⸻

Nächste Schritte
	•	Spalten flexibler erkennen (zb. Mapping statt fixer Namen)
	•	UI besser aufteilen
	•	insgesamt robuster gegen unterschiedliche Daten machen