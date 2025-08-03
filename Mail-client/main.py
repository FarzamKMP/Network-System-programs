import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

server = smtplib.SMTP('SMTP.YOUR-DOMAIN.COM', 587)

server.ehlo()

server.login('YOUR.EMAIL@mail.com', 'YOUR_PASSWORD')

msg = MIMEMultipart()
msg['From'] = 'Amirfarzam'
msg['To'] = 'amirfarzamkmp@proton.me'
msg['Subject'] = 'Test Email'
body = 'This is a test email with an attachment.'
msg.attach(MIMEText(body, 'plain'))
filename = 'YOURFILE.txt'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(part)
server.sendmail('YOUREMAIL@mail.com', 'TO.EMAIL@email.com', msg.as_string())
attachment.close()
server.quit()
print("Email sent successfully!")                