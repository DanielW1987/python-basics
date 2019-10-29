import smtplib
from email.mime.text import MIMEText

body: str = "This is a text email."
message: MIMEText = MIMEText(body)
message["From"] = "no-reply@gmail.com"
message["To"] = "dummy@gmail.com"
message["Subject"] = "Hello"

server: smtplib.SMTP = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user="user", password="pass")
server.send_message(message)
