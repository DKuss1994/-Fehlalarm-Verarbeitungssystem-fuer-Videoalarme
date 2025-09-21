# 🖼️ Screen2Mail

**Screen2Mail** verarbeitet Screenshots automatisch, sortiert sie und verschickt sie per E-Mail – ideal für Alarm- oder Monitoring-Systeme.  

---

## 📦 Installation

1. Installiere [Python 3](https://www.python.org/downloads/).  
2. Repository klonen:  
```bash
git clone https://github.com/DKuss1994/-Fehlalarm-Verarbeitungssystem-fuer-Videoalarme.git
cd -Fehlalarm-Verarbeitungssystem-fuer-Videoalarme
```
3. Abhänigkeiten installieren:
```bash
pip install pandas openpyxl cryptography
```

⚙️ Einrichtung

1. Dateipfade anpassen (Haupprogramm.py):
```bash
inputs_dir = "/Pfad/zu/Screenshots"
base_output_dir = "/Pfad/zu/Ablage"
excel_path = "/Pfad/zu/Kundedaten.xlsx"
```
2. E-Mail-Konfiguration (send_email.py):
sender → Absenderadresse

smtp_server → z.B. smtp.web.de

username → Login-E-Mail

3. Optional: Passwortverschlüsselung mit PasswortManager aktivieren

🚀 Verwendung

1. Screenshots in das Eingangsverzeichnis (inputs_dir) legen.

2. Programm starten:
```bash
python Haupprogramm.py
```
3. Das passiert automatisch:

  - Screenshots umbenennen: ID_Beschreibung_Zeitstempel.ext
  
  - Verschieben in Unterordner nach ID-Bereich & Beschreibung
  
  - Kundendaten aus Excel auslesen
  
  - E-Mail mit Screenshot verschicken

✨ Features

  - Umbenennung der Screenshots mit Zeitstempel
  
  - Ordnerstruktur nach ID-Bereich & Beschreibung
  
  - Kundendaten aus Excel abrufen
  
  - Automatischer E-Mail-Versand mit Betreff, Body & Anhang
  
  - Passwortverschlüsselung für E-Mail-Login
  
  - Vollautomatischer Ablauf über main()

🛠 Technologien

  - Python 3
  
  - Pandas & openpyxl → Excel
  
  - smtplib & email → E-Mail-Versand
  
  - cryptography.Fernet → Passwortverschlüsselung
  
  - os, shutil, datetime → Datei-Management
  
  📂 Beispiele

Dateibenennung:
```bash
12101_Videofehlalarm_21.09.2025_15-30-22.jpg
```
Ordnerstruktur:
```bash
Videoalarme/
  12100-12199/
    12101/
      Videofehlalarm/
        12101_Videofehlalarm_21.09.2025_15-30-22.jpg
```

E-Mail-Body:
Sehr geehrte Damen und Herren,

es wurde ein Alarm ausgelöst:
- Objekt: Musterobjekt
- ID: 12101
- Beschreibung: Videofehlalarm
- Zeit: 21.09.2025_15-30-22

Im Anhang finden Sie den Screenshot.

Mit freundlichen Grüßen,
Ihre Leitstelle

📄 Lizenz

MIT License


