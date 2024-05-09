import smtplib

def sendmail(email):
    TO = email
    SUBJECT = 'Suggestions about Fashion Recommendation System'
    TEXT ="Thank you for your valuable feedback"
     
    print(TEXT)
    # Gmail Sign In
    gmail_sender = "moulalicce225@gmail.com"
    gmail_passwd = "wzvlnzkfebqafliw"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()
