#!/usr/bin/env python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor



# Email config
sender_email = "datafuseai632@gmail.com"
recipient_email = "santoskrm567@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port =  587 
smtp_username = "datafuseai632@gmail.com"
smtp_password = "yaxx yesv rula zluq"




def send_email(subject, message):
        # return
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        server=None
        try:
            # Create a secure SSL/TLS connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

                # Login to your email account
            server.login(smtp_username, smtp_password)

                # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())

            print(f"Email sent successfully!")

        except Exception as e:
            print(f"An error occurred while sending the email: {str(e)}")

        finally:
           if server:
                # Close the connection to the SMTP server
                server.quit()

def send_emails():
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        for i in range(30):
            executor.submit(send_email, "test subject", "this is a test subject")

# Call the function to send emails
send_emails()
print("hello")