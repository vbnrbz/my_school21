from src.config_4 import Configuration
import json
from typing import Dict

def main() -> Dict[str, str]:
    config: Configuration = Configuration()
    with open(f'{config.base_folder}/{config.login}.json', encoding='utf-8') as file:
        return json.load(file)

if __name__ == '__main__':
    main()