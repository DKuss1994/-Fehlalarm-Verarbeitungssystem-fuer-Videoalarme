import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from Vorlage import PasswortManager

#pw_v.erstelle_key()
#pw_v.verschlüssel_password(#Hier einfach passwort eingeben als String)



def send_email(receiver: str, subject: str, body: str, attachment: str = None):
    sender = "kussdennisubi@web.de"
    pm = PasswortManager(key_file="mail_schlüssel", enc_file="mail_pw")
    password = pm.lade_password()
    smtp_server = "smtp.web.de"
    port = 587
    username = "kussdennisubi@web.de"
    # Nachricht vorbereiten
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"]= subject

    # Text einfügen
    msg.attach(MIMEText(body, "plain"))

    # Anhang hinzufügen, wenn vorhanden
    if attachment:
        with open (attachment, "rb") as f:
             part = MIMEBase("application", "octet-stream")
             part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",f"attachment, filename={os.path.basename(attachment)}")
        msg.attach(part)

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls() # sichere Verbindung
            server.login(username, password)#login
            server.send_message(msg)
            print(f"E-Mail an {receiver} verschickt mit Anhang={bool(attachment)}")
