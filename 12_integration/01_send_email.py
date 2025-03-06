import smtplib
from email.mime.text import MIMEText

port = 587
smtp_server = "smtp-relay.brevo.com"
login = "64f34f001@smtp-brevo.com"
password = "5Pbnhz1YNG8wODfX"

sender_email = "info@samantha.com"
receiver_email = "roxivi6016@calmpros.com"

email_list = ["abc@gmail.com, xyz@gmail.com"]

text = """
    hello, this mail send from my python application
"""

message = MIMEText(text, "plain")
message["Subject"] = "hello"
message["From"] = sender_email
message["To"] = receiver_email
# message["To"] = ",".join(email_list)

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("send mail")