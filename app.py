import requests 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from os.path import basename
import time 




def main(): 
    print("Program Start")
    #Set websites to health check 
    urls = []
    
    #List of clients?
    Clients = []
    #List of internal contacts? 
    internals = []
    #Provide a user agent to bypass built in security features 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


    while True: 
        for i in urls: 
            
            try: 
                r = requests.get(url = i, headers=headers)
                if r.status_code != 200: 
                    if i == '': 
                        Send_Email('', i)
                        #Alert me just in case 
                        Send_Email('', i)
                        #Watch Dog alerts 
                        continue 

                    if i == '': 
                        Send_Email('', i)
                        #Alert me, just in case 
                        Send_Email('', i)
                        #Watch dog alerts 
                        continue 

                    Send_Email('', i)

                else: 
                    #Nomral status code, go next 
                    continue 

            except: 
                print("ERROR On URL Request outbound, check internet connection")

            #Wait sometime before next requests 
            time.sleep(5)

        #Sleep for 20 minutes 
        time.sleep(1200)

    print("Program End")




def Send_Email(Toes, url):
    sender = ''

    smtpObj = smtplib.SMTP('',port='587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender,'')

    try:
        msg = MIMEMultipart()
        msg['Subject'] = url + ' Website is experiencing an outage!'
        message = url + " is currently experiencing an outage. This outage was reported by the URI Health Check Software. URI health check software is a trivial watch dog script that sends a simple GET request to a pre-determined URL. If the URL returns a non 200 HTTP response then the watchdog software alerts a pre-defined list of emails."
        
        msg.attach(MIMEText(message))


        smtpObj.sendmail(sender, Toes, msg.as_string())
        smtpObj.quit()    
    except:
        print("ERROR")



if __name__ == '__main__': 
    main() 
