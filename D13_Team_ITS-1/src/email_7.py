from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from src.config_6 import SMTPSettings


class EmailMessage:
    def __init__(self, from_email: str, to_email: str, subject: str, body: str) -> None:
        self.from_email: str = from_email
        self.to_email: str = to_email
        self.subject: str = subject
        self.body: str = body

    def create_mime_message(self) -> MIMEMultipart:
        msg: MIMEMultipart = MIMEMultipart()
        msg['From']: str = self.from_email
        msg['To']: str = self.to_email
        msg['Subject']: str = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        return msg

class EmailSender:
    def __init__(self, smtp_settings: SMTPSettings) -> None:
        self.smtp_settings: SMTPSettings = smtp_settings

    def send_email(self, txt: EmailMessage) -> None:
        try:
            msg: MIMEMultipart = txt.create_mime_message()

            with smtplib.SMTP(self.smtp_settings.server, self.smtp_settings.port) as server:
                server.starttls()
                server.login(self.smtp_settings.email, self.smtp_settings.email_password)
                server.send_message(msg)

            print('The letter has been sent successfully')
        except Exception as ex:
            print('Failed to send email!')

