import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("prepareraj@gmail.com","956956956")

fromaddr = "prepareraj@gmail.com"
toaddr = "selftuts@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "New Blog Post Found"




class EmailService:
    def __init__(self):
        # sending email
            body = "{} New Blogs under the tags :  {}".format(totalNewPost,postIdentifiers)

            msg.attach(MIMEText(body, 'plain'))

            text = msg.as_string()

            data = server.sendmail("prepareraj@gmail.com", "selftuts@gmail.com", text)
