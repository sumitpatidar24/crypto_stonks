import smtplib, ssl 

def sende(msg):
    context = ssl.create_default_context()
    port = 465 
    password = "piroorip#24"
    sender_email = "piro0orip@gmail.com"
    receiver_email = "sumitpatidarec18@acropolis.in"
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, msg)
        print("Email sent")
