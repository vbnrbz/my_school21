from email.mime.multipart import MIMEMultipart
from email_6 import EmailMessage
from config_6 import SMTPSettings

def main() -> MIMEMultipart:
    mail: str = input('Enter patient email: ')
    smtp: SMTPSettings = SMTPSettings()
    ex: EmailMessage = EmailMessage(smtp.email, mail, 'Receipt', 'Test')

    return ex.create_mime_message()

if __name__ == '__main__':
    main()