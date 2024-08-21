
import smtplib
import random




otp=''.join([str(random.randint(0,9)) for i in range(4)])
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('pythonproject0246@gmail.com','Python0246')
msg='hello your otp is :'+str(otp)
server.sendmail('pythonproject0246@gmail.com','jagannathsarmalkar33831@gmail.com',msg)
server.quit()