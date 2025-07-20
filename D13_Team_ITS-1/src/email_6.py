from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

