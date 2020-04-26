from worker import celeryApp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#server = smtplib.SMTP('smtp.gmail.com', 587)
#server.starttls()
#server.login("prepareraj@gmail.com","956956956")
#
#fromaddr = "prepareraj@gmail.com"
#toaddr = "selftuts@gmail.com"
#msg = MIMEMultipart()
#msg['From'] = fromaddr
#msg['To'] = toaddr
#msg['Subject'] = "New Blog Post Found"


@celeryApp.task
def sendEmail(context):
    
    uniquePost = context.get('uniquePosts',[])
    if len(uniquePost) == 0 :
        return context
    
    emailBody = "{} New Blogs under : {}"
    
    indetifierList = []

    for eachData in uniquePost :
        if indetifierList.count(eachData['identifier']) == 0 :
            indetifierList.append(eachData['identifier'])
    
    text = ",".join(indetifierList)

    body = "{} New Blogs under the tags :  {}".format(len(uniquePost),text)

    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()

    data = server.sendmail("prepareraj@gmail.com", "selftuts@gmail.com", text)
    print("!!!!!!!!!!!!!!!")
    print("email sent")
    
    return context
