import ai_gigachat
import article

class Summarizer:
    def __init__(self):
        ai_gigachat.connect_gigachat()

    def __article_to_text(self, link):
        return article.article_to_text(link)

    def __send_gigachat(self, text):
        system_text = '''
Ты — опытный аналитик, который умеет создавать краткие и информативные конспекты больших текстов. Прочитай текст статьи и создай конспект не длиннее 200 слов на русском языке, следуя инструкциям:

1. Основная тема статьи: В одном предложении опиши, о чем эта статья.
2. Ключевые идеи: Перечисли 3-5 ключевых идей или выводов, которые автор делает в статье.
3. Методы/подходы: Если в статье описываются методы, подходы или эксперименты, кратко опиши их.
4. Результаты: Какие результаты или выводы представлены в статье?
5. Значимость: Почему эта статья важна? Какое влияние она может оказать на область исследования?
'''
        user_text = text

        return ai_gigachat.ask_gigachat(system_text, user_text)

    def summarize(self, link) -> str:
        return self.__send_gigachat(self.__article_to_text(link))

if __name__ == '__main__':      
    print(Summarizer().summarize('https://arxiv.org/html/2502.01630'))