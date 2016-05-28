import smtplib
import sys
import getpass

fromaddr = input('From: ')
toaddrs = input('To: ')
subj = input('Subject: ')
print('Enter the message content, end with EOF')
msg = ''
while True:
    currLine = input()
    if currLine == 'EOF':
        break
    else:
        msg += currLine
msg = '\r\n'.join(['From: {}'.format(fromaddr), 'To: {}'.format(toaddrs), 'Subject: {}'.format(subj), msg])
password = getpass.getpass('Enter the passwd: ')
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    print('Email sent successfully!')
except:
    print('Did not success!')
