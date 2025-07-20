import requests
from bs4 import BeautifulSoup

# Это своя ошибка NotAvailable
class NotAvailable(Exception):
    pass

def article_to_text(link):
    response = requests.get(link)
    if response.status_code != 200:
        raise NotAvailable('Статья недоступна.')
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.get_text()

if __name__ == '__main__':
    link = 'https://arxiv.org/html/2502.02633v1'
    error_link = 'https://arxiv.org/html/asldkasmdaksldlamsdklmamsdlkmalsmkdlamsmdasldmlamsdlkmaklsmdlma'

    print(article_to_text(link))