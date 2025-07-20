from email_7 import EmailSender, EmailMessage
from config_6 import SMTPSettings

def main() -> None:
    mail: str = input('Enter patient email: ')
    smtp: SMTPSettings = SMTPSettings()
    e: EmailSender = EmailSender(smtp)
    e.send_email(EmailMessage(smtp.email, mail, 'Receipt', 'Test'))


if __name__ == '__main__':
    main()