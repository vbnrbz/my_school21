## Документация

Приложение представляет собой веб-сервис, реализованный с использованием фреймворка Django. Оно предназначено для прогнозирования вероятности инсульта на основе различных данных пациента и предоставления рекомендаций по улучшению здоровья с использованием внешнего API (GigaChat).

### Структура приложения
- model.pkl - файл с уже обученной моделью, с которой можно работать
- model.ipynb - файл, в котором анализируется датасет и обучается модель
- data/healthcare-dataset-stroke-data.csv - датасет
- project - сайт на Django
- tests - директория с тестами

### Как запустить сайт
1. Открыть папку проекта и правильно выбрать интерпретатор.
2. Ввести в терминале:
`cd src/final_project/project`
3. Ввести в терминале:
`python3 manage.py runserver`
4. Перейти в браузер по адресу `127.0.0.1:8000`.
5. Начать ввод данных и нажать кнопку отправить.

### Структура база данных
Название таблицы - app_main, используется SQLite3
- gender (пол): Male, Female
- age (возраст): 0 - 120
- hypertension (наличие гипертензии): 0, 1
- heart_disease (наличие сердечно-сосудистых заболеваний): 0, 1
- ever_married (был ли пациент когда-либо в браке ): False, True
- work_type (тип работа): children, Govt_jov, Never_worked, Private, Self-employed
- residence_type (тип местности): Rural, Urban
- avg_glucose_type (средний уровень глюкозы): 0 - 999
- bmi (индекс массы тела): 0 - 99
- smoking_status (статус курения): formerly smoked, never smoked, smokes, Unknown 
- stroke_prediction (вероятность инсульта): 0 - 100
Данные загружаются в базу данных при помощи DjangoORM после POST-запроса.