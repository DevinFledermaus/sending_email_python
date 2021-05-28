import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'd.e.fledermaus86@gmail.com'
receiver_email_id = 'aneeqahjones2@gmail.com, jasoncee017@gmail.com, thapelo@lifechoices.co.za'
password = input("Enter your password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "This is my attempt at sending to multiple recipients\n"
body = body + "Hope this works"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email_id, password)

# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)

# terminating the session
s.quit()
