# Screen2Mail
Screen2Mail ist ein Projekt, was einfach und schnell Screenshots versenden soll per Mail.

---

## Inhaltsverzeichnis
- [Installation](#installation)
- [Einrichtung](#einrichtung)
- [Verwendung](#verwendung)
- [Features](#features)
- [Technologien](#technologien)
- [Beispiele](#beispiele)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)
- [Kontakt](#kontakt)
  
---
## Installation  

1. Installiere [Python](https://www.python.org/downloads/) Version 3.xx
2. Prüfe ob git installiert ist mit dem Terminalbefehl: git --version
  - Wenn du git installiert hast:
    - Kopiere: git clone https://github.com/DKuss1994/-Fehlalarm-Verarbeitungssystem-fuer-Videoalarme.git
      und gib es im Terminal ein
    - Kopiere: cd -Fehlalarm-Verarbeitungssystem-fuer-Videoalarme
      und gib es im Terminal ein
---
## Einrichtung
  Jetzt muss das Programm noch eingerichtet werden, da ich noch kein Erstellungs Programm habe muss man das Manuell machen.
  - Wir benötigen 3 Dateipfade.
    - Einmal in der Variable Zeile 7 Hauptprogramm inputs_dir = Hier ist der Ordner wo die Screenshots abgelegt werden sollen. Einfach ein Ordner anlegen und den Dateipfad hier hinterlegen.
    - Einmal in der Variable Zeile 8 Hauptprogramm base_output_dir = Hier werden die Screenshoots in Ordnerstrukturen hinsortiert.
    - Einmal in der Variable Zeile 9 Hauptprogramm excel_path = Hier benötigten wir die csv Dateipfad wo das Programm die Stammdaten herbekommt.
  - In send_email.py müssen Divere Änderungen vorgennomen werden:
    - Der Variabele 15 sender muss angepasst werden. Mit der Mailadresse, die der Empfänger sieht
    - Variable 18 smtp_server muss an dein server angepasst werden ich hab hier web.de genommen.
    - Variable 20 Username musst du anpassen. Das ist deine Email
  - Du benötigst die Verschlüssung nicht unbedingt, wenn du das Projekt nicht öffentlich zeigen willst, aber ich würde es empfehlen
    
  
  
