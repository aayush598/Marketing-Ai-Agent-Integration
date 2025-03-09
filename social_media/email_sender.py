import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

class EmailSender:
    """
    Handles sending emails via Gmail SMTP.
    """
    def __init__(self):
        self.sender_email = os.getenv("SENDER_MAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        if not self.sender_email or not self.sender_password:
            raise ValueError("❌ Missing email credentials in .env file!")

    def send_email(self, recipient_email: str, subject: str, body: str) -> bool:
        """
        Sends an email using Gmail SMTP.
        """
        try:
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            print("✅ Email sent successfully!")
            return True

        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False

# Test the function if running this script directly
if __name__ == "__main__":
    email_client = EmailSender()
    success = email_client.send_email(
        recipient_email="raiseracademy.sap@gmail.com",
        subject="Automated Email",
        body="Hello, this is an automated email sent using Python."
    )
    if success:
        print("✅ Test Email sent successfully!")
    else:
        print("❌ Test Email failed!")
