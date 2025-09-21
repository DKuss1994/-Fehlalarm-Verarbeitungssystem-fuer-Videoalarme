from datetime import datetime
import os
import shutil # Fürs verschieben
from excel_utilis import load_customer_data
from send_email import send_email

inputs_dir = r"C:\Users\kussd\Desktop\Videoordner" # Hier kommen die Scrennshoots rein
base_output_dir = r"C:\Users\kussd\Desktop\Video" #Hier werden Sie rein Sortiert
excel_path = r"C:\Users\kussd\Desktop\Video\Datenbank.xlsx"
def creation_dt(p):
    # Hole Erstellungzeit der Datei
    ts = os.path.getctime(p) # hier legen wir mit os.path.getctime den Time code in die Variable TS
    # Formatiere das Dati, hübsch als String.
    return datetime.fromtimestamp(ts).strftime("%d.%m.%Y_%H-%M-%S")


# Hier wollen wir den Screenshot umbennen. P ist die Variable für den Screenshot.
def rename_file(p):
    """Bennenung: ID_Beschreibung_Zeitstempel.ext"""
    filename = os.path.basename(p)# Hier nehmen wir den basenamen aus dem Screenshot raus
    name, ext = os.path.splitext(filename)#hier wird der Screnshot in den jeweiligen begrigg name und funktion sowas wie .jpg getrennt
    # Erwartet: 12101_straftat.jpg oder 12101.jpg
    parts = name.split("_")
    file_id = parts[0] # Wichtig ist in unserem Programm, dass die ID immer das erste ist was wir eingeben und darnach den _
    beschreibung = parts[1] if len(parts)> 1 else "Videofehlalarm" #Hier kommen Texte die nach den _ kommen
    ts = creation_dt(p) # Hier nehmen wir einfach TS für Zeitstempel und durch unsere Funktion creation_dt (p) wo p immer die Screenshot datei ist erstellen speichern wir den Zeitstempel.
    new_name = f"{file_id}_{beschreibung}_{ts}{ext}"#Hier wird jetzt alles zusammen gefügt id, beschreibung und der Zeitstempel mit der .jpg endung
    return new_name, file_id, beschreibung # Wichtig ist, dass wir new_name file_id und beschreibung übergeben. ID und beschreibung für die Ordner Struktur
def move_file(p, new_name, file_id,beschreibung):
    """Verschiebt die Datei in die Zielstruktur"""
    #Bereich berechnen (z.B. 12101 -> 12100 - 12199)
    id_num = int(file_id) # hier machen wir aus dem strin eine Ganzzahl
    lower = (id_num//100) * 100 #Das doppel // nimmt nur ganze zahlen, so dass wir bei 6666 auf 66kommen und 66*100 6600
    upper = lower + 99
    bereich_folder = f"{lower}-{upper}"

    #Zielordner zusammensetzen
    target_dir = os.path.join(base_output_dir, bereich_folder, file_id, beschreibung)

    os.makedirs(target_dir, exist_ok=True)
    #Neuer Dateiname + Zielpfad
    target_path = os.path.join(target_dir, new_name)

    shutil.move (p, target_path)
    print (f"Verschoben: {p} -> {target_path}")
    return target_path

def main():
    for file in os.listdir(inputs_dir):
        p = os.path.join(inputs_dir,file)
        if os.path.isfile(p):
            new_name, file_id, beschreibung = rename_file(p)
            target_path = move_file(p, new_name, file_id, beschreibung)
            customer = load_customer_data(excel_path, int(file_id))
            if not customer:
                print(f"X Keine Kundendaten für ID {file_id} gefunden. Bitte nachtragen")
                continue
            receiver = customer["E-Mail-Adresse-Kunde"]
            objekt_name = customer.get("Objekt-Name", "Unbekanntes Objekt")

            subject = f"Alarmmeldung {objekt_name} ({file_id})"
            body = f"""Sehr geehrte Damen und Herren,
            
es wurde ein Alarm ausgelöst:
- Objekt: {objekt_name}
- ID: {file_id}
- Beschreibung: {beschreibung}
- Zeit: {creation_dt((target_path))}

Im Anhang finden Sie den zugehörigen Screenshot

Mit freundlichen Grüßen

Ihre Leitstelle
"""
            send_email(
                receiver=receiver,
                subject=subject,
                body=body,
                attachment=target_path
            )

if __name__ == "__main__":
    main()
