import smtplib

gmail_user = 'siddharth.lh@gmail.com'  
gmail_password = 'IlikeToDrinkTomatoSoup'

sent_from = gmail_user  
to = ['siddharth.lh@gmail.com', 'siddharth.lh@gmail.com']  
subject = 'You need to get this'  
body = " Hey, whats \n up? "

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('mail sent!')
except:  
    print('mail fail...')



# ideas could be send emergency mail,etc.
