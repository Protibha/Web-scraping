import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['Subject']='Amazon Reviews Webscraped data results'
msg['From']='SIGCE SYCE Girls team'
msg['To']='sigcegirls@gmail.com'

with open('EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)


with open("reviews.csv","rb") as f:
    file_data=f.read()
    #print("File data in binary",file_data)
    file_name=f.name
    print("File name is",file_name)
    msg.add_attachment(file_data,maintype="application",subtype="csv",filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("sigcegirls@gmail.com","pnyfdqoisnslxbbk")
    server.send_message(msg)
    
print("Email sent !!")
    
    
    