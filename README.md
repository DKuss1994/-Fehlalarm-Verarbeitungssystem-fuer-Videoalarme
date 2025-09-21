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
      
   - Alternativ einfach die Codeschnippsel kopieren und einfügen von:
     
    - Haupprogramm.py
     
    - Vorlagen.py
    
    - excel_utilitis.py
    
    - send_email.py
     
---
## Einrichtung
  Jetzt muss das Programm noch eingerichtet werden, da ich noch kein Erstellungs Programm habe muss man das Manuell machen.
  - Wir benötigen 3 Dateipfade.
    - Einmal in der Variable Zeile 7 Haupprogramm inputs_dir = Hier ist der Ordner wo die Screenshots abgelegt werden sollen. Einfach ein Ordner anlegen und den Dateipfad hier hinterlegen.
    - Einmal in der Variable Zeile 8 Haupprogramm base_output_dir = Hier werden die Screenshoots in Ordnerstrukturen hinsortiert.
    - Einmal in der Variable Zeile 9 Haupprogramm excel_path = Hier benötigten wir die csv Dateipfad wo das Programm die Stammdaten herbekommt.
  - In send_email.py müssen Divere Änderungen vorgennomen werden:
    - Der Variabele 15 sender muss angepasst werden. Mit der Mailadresse, die der Empfänger sieht
    - Variable 18 smtp_server muss an dein server angepasst werden ich hab hier web.de genommen.
    - Variable 20 Username musst du anpassen. Das ist deine Email
  - Du benötigst die Verschlüssung nicht unbedingt, wenn du das Projekt nicht öffentlich zeigen willst, aber ich würde es empfehlen.
    - Bei Passwortverschlüssung importiere Aus vorlage den PasswortManager
    - Im PasswortManager musst du dein key_file und deine enc.file bennen. key_file = in str ist der Schlüssel der die Chiffre freischaltet. enc.file= in str ist dein Verschlüsseltes Passwort, nicht wundern für beide wird eine neue Datei erstellt.
    - Dann erstellst du den key_file im PasswortManger mit pw.erstelle_key() und mit pw.verschlüssel_password verschlüsselt dein Password. 
      ```Bash
     
      
      
      def send_email(receiver: str, subject: str, body: str, attachment: str = None):
          sender = "kussdennisubi@web.de"
          pm = PasswortManager(key_file="mail_schlüssel", enc_file="mail_pw")
          pw.erstelle_key()
          pw.verschlüssel_password(#Hier einfach passwort eingeben als String)
          password = pm.lade_password()
      ```
    Nach dem die beiden Filse erstellt wurden kannst du pw.erstelle_key() und vor allem pw.verschlüssel_password raus löschen.
    WICHTIG lade_password() benutzt den Key und das verschlüsselte Passwort um dein Password zu erstellen. Nie dein Password klar zeigen, wenn du z.b.
    ```Bash
    print(lade_password) # Dein Klarpasswort wird in der Konsole angezeigt
    ```
    Aber nur Person, die beide Files haben können sich das anzeigen lassen.
    
Wir müssen noch eine CSV Datei erstellen 
Wichtig an der CSV datei ist:
- Das Objekt-ID,	E-Mail-Adresse-Kunde und	Objekt-Name genau so benannt in der 1 Zeile stehen hier ein Beispiel:
![Screenshot_2](https://github.com/user-attachments/assets/9ff20e49-436a-4dd9-a202-04b8a4055988 )

---
## Verwendung
  1. Screenshot-Verarbeitung
    - Umbenennung mit ID, Beschreibung und Zeitstempel.
  
  2. Ordnerstruktur & Ablage
    - Verschiebt Screenshots automatisch in Unterordner nach ID-Bereich und Beschreibung.
  
  3. Kundendaten-Integration
    -Liest Kundendaten aus Excel (E-Mail, Objektname).
    -Prüft, ob Daten vorhanden sind.
  
  4. E-Mail-Versand
    - Versendet Screenshots per SMTP mit Betreff, Body und Anhang.
    - Nutzt verschlüsseltes Passwort für Login.

## Features

1. Screenshot-Verarbeitung

  - Benennt Screenshots um: ID_Beschreibung_Zeitstempel.ext.
  
  - Nutzt Erstellungsdatum für Zeitstempel.

2. Ordnerstruktur & Ablage

   - Organisiert Dateien automatisch nach ID-Bereichen und Beschreibung.
    
   - Erstellt fehlende Ordner automatisch.

3. Kundendaten-Integration

    - Liest Daten aus Excel (E-Mail, Objektname).
    
    - Prüft, ob Kundendaten vorhanden sind.

4. E-Mail-Versand

    - Sendet Screenshot per SMTP mit Betreff, Body und Anhang.
    
    - Nutzt verschlüsseltes Passwort für sichere Anmeldung.

5. Passwort-Management

    - Verschlüsselt und speichert Passwörter sicher mit Fernet.

6. Automatisierung

    - Alles läuft automatisch über main(), modular aufgebaut für Umbenennung, Ablage, Datenabfrage und Versand.
