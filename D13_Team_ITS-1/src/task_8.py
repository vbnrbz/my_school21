from src.doctor_5 import Doctor
from src.config_6 import Configuration, SMTPSettings
from src.email_7 import EmailSender, EmailMessage


def main() -> None:
    config: Configuration = Configuration()
    doc: Doctor = Doctor(config)

    saving: str = input('Do I need to save the recipe to a file? ')
    if saving:
        file_name: str = input('Enter the name of the file where the recipe will be saved: ')
        x: str = doc.write_recipe(file_name)
    else:
        x: str = doc.write_recipe()

    mail: str = input('Enter patient email: ')
    smtp: SMTPSettings = SMTPSettings()
    e: EmailSender = EmailSender(smtp)
    e.send_email(EmailMessage(smtp.email, mail, 'Receipt', x))

if __name__ == '__main__':
    main()