from src.config_4 import Configuration
from src.doctor_5 import Doctor

def main() -> str:
    config: Configuration = Configuration()
    doc: Doctor = Doctor(config)

    saving: str = input('Do I need to save the recipe to a file? ')
    if saving:
        file_name: str = input('Enter the name of the file where the recipe will be saved: ')
        x: str = doc.write_recipe(file_name)
    else:
        x: str = doc.write_recipe()

    return x

if __name__ == '__main__':
    print(main())