'''
import smtplib
from email.mime.text import MIMEText
from getpass import getpass
def send_email():
 msg = MIMEText(''''''LPGA에서 처음으로 파4홀 홀인원이 나왔다고 합니다.'''''')
 msg['Subject'] = '피로그래밍 4기'
 msg['From'] = 'sarkmen@naver.com'
 msg['To'] = 'ask@festi.kr'
 password = getpass('Password : ')
 server = smtplib.SMTP("smtp.naver.com", 587)
 server.ehlo()
 server.starttls()
 server.login('sarkmen@naver.com', password)
 server.send_message(msg)
 server.close()
if __name__ == '__main__':
 send_email()

'''

import smtplib
from email.mime.text import MIMEText
from getpass import getpass

def send_email():
 msg = MIMEText('''안녕하세요.
May the django be with you.
Life is short, use Python.''')
 msg['Subject'] = '피로그래밍 4기'
 msg['From'] = 'sarkmen@naver.com'
 msg['To'] = 'ask@festi.kr'
 password = getpass('Password : ')
 server = smtplib.SMTP("smtp.naver.com", 587)
 server.ehlo()
 server.starttls()
 server.login('sarkmen@naver.com', password)
 server.send_message(msg)
 server.close()

if __name__ == '__main__':
 send_email()