import smtplib
from email.message import EmailMessage



    # email_subject = "Email test from Python" 
    # sender_email_address = "your_email@gmail.com" 
    # receiver_email_address = "receiver_email@address.com" 


def sendEmail(email_subject, receiver_email_address, result, user):
    message = EmailMessage()

    sender_email_address = "vivi_enda@outlook.com"
    email_password = "vivienda123" 
    
    # Configure email headers 
    message['Subject'] = email_subject 
    message['From'] = sender_email_address 
    message['To'] = receiver_email_address

    # Set email body text 
    # ESTO ES PARA TEXTO PLANO, VER DE PRUEBA
    message.set_content("Hola "+ str(user) +", \nEstos son los alquileres que encontramos que se ajustan a tus necesidades \n"+ str(result)[1:-1] + "\n Saludos!")
    # Set smtp server and port
    email_smtp = "smtp.office365.com"  
    server = smtplib.SMTP(email_smtp, '587')

    # Identify this client to the SMTP server 
    server.ehlo() 
    # Secure the SMTP connection 
    server.starttls()
    
    # Login to email account 
    server.login(sender_email_address, email_password) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()

