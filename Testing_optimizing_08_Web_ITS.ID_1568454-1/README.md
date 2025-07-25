# Тестирование и оптимизация

Аннотация: в этом проекте ты изучишь инструменты тестирования.

## Содержание

1. [Chapter I](#chapter-i) \
   1.1. [Рекомендации к проекту](#рекомендации-к-проекту)
2. [Chapter II](#chapter-ii)
3. [Chapter III](#chapter-iii) \
   3.1. [Задание 1](#задание-1-написание-юниттестов-для-djangoприложения) \
   3.2. [Задание 2](#задание-2-функциональное-тестирование-api) \
   3.3. [Задание 3](#задание-3-настройка-линтера-для-djangoпроекта) \
   3.4. [Задание 4](#задание-4-добавление-логирования-в-djangoприложение) \
   3.5. [Задание 5](#задание-5-добавление-кеширования-в-djangoприложение) \
   3.6. [Задание 6](#задание-6-тестирование-reactкомпонентов) \
   3.7. [Задание 7](#задание-7-настройка-eslint-и-исправление-ошибок-линтера)


## Введение 

Приложение для клиники «Здоровый дух» казалось почти готовым, и ты был рад, что вскоре попрощаешься с Вениамином и Клариссой (хотя они и были в целом милыми людьми). Однако сегодня тебя разбудил звонок в 7 утра:

>— Я что-то нажала, и все исчезло...
>>**Кларисса**

Спросонья ты не совсем понимал, кто это, что она нажала и что могло исчезнуть. Однако в следующее мгновение ты осознал: возникла какая-то проблема с приложением. Сон как рукой сняло. 

>— Что именно вы нажали, и что произошло?
>>**Стажер**

>— Я хотела создать нового врача, но приложение заглючило и выдало ошибку ни с того ни с сего. Хотя вчера такого не было. Неужели все сломалось?
>>**Кларисса**

>— Не паникуйте, скорее всего, какая-то ошибка в обработке данных. 
>>**Стажер**

Сам же ты лихорадочно прокручивал в голове, что именно могло сломаться, пока поспешно собирался на работу. В свой законный выходной. Наверное, стоило, как советовали коллеги, провести тестирование системы... Даже обидно, что ты вспомнил об этом только в субботу, теперь придется все исправлять, потому что сроки уже горели. 

## Chapter I

### Рекомендации к проекту

Как учиться в «Школе 21»:

- На протяжении всего курса ты будешь самостоятельно добывать информацию. Пользуйся всеми доступными средствами поиска информации, к примеру, Google и GigaChat. Будь внимателен к источникам информации: проверяй, думай, анализируй, сравнивай.
- Взаимообучение (P2P, Peer-to-Peer) — это процесс, при котором учащиеся обмениваются знаниями и опытом, выступая одновременно в роли учителей и учеников. Этот подход позволяет учиться не только у преподавателя, но и друг у друга, что способствует более глубокому пониманию материала.
- Не стесняйся просить помощи: вокруг тебя такие же пиры, которые тоже проходят этот путь впервые. Не бойся откликаться на просьбы о помощи. Твой опыт ценен и полезен, смело делись им с другими участниками.
- Не списывай, а если пользуешься помощью — всегда разбирайся до конца, почему, как и зачем. Иначе твое обучение не будет иметь никакого смысла.
- Если ты на чем-то застрял и кажется, что все уже перепробовал, но по-прежнему непонятно, куда идти, — просто передохни! Поверь, этот совет помогал многим разработчикам в их работе. Проветрись, перезагрузи голову, и, возможно, в следующий раз тебе наконец придет нужное решение!
- Важен не только результат обучения, но и сам процесс. Нужно не просто решить задачу, а понять, КАК ее решить.

Как работать с проектом:
- Вся работа выполняется на виртуальной машине. Для начала ее нужно настроить, воспользовавшись [инструкцией](https://applicant.21-school.ru/guide_vm_med). Далее запустить виртуальную машину и продолжать выполнять работу над проектом там.
- Перед выполнением проект необходимо склонировать с GitLab в одноименный репозиторий.
- Все файлы с кодом необходимо создавать в папке src склонированного репозитория.
- После клонирования проекта необходимо создать ветку `develop` и вести разработку в ней. После этого пушить в GitLab также нужно ветку `develop`.
- В твоей директории не должно быть иных файлов, кроме тех, что обозначены в заданиях.

Дисклеймер:

- Наша команда не медики. Если ты будешь видеть в тексте медицинские неточности или ошибки, заранее просим у тебя прощения. Оставляй нам обратную связь, и мы все поправим!
- Иногда повествование ведется в несколько шутливой форме, чтобы не было скучно. Однако, как ты и сам знаешь, юмор и шутки — субъективная вещь. Поэтому если каламбуры в данном тексте, по твоему мнению, попахивают батиным юмором, то, пожалуйста, просто прими это.

## Chapter II

Тестирование — это отдельная дисциплина, в которой есть несколько разных разделов: ручное тестирование, автоматизированное тестирование, функциональное тестирование, регрессионное тестирование, нагрузочное тестирование, тестирование безопасности и приемочное тестирование. Каждый из этих разделов обладает своими особенностями, методологиями и инструментами. Есть специалисты, которые берут на себя эти обязательства после того, как разработчик написал код.

**На тему тестирования есть свой [ГОСТ](https://docs.cntd.ru/document/1306397049).**

Но перед тем как отдавать задачу в тестирование, хорошей практикой является потестировать самому и написать тесты. На реальных проектах есть этапы CI/CD, один из которых — запуск тестов. Если тесты не пройдут — упадет сборка и будет уведомление о непройденных тестах. Это будет означать, что надо их пофиксить, прежде чем отдавать на повторную сборку.

Удобно (хотя иногда и больно), если тесты написаны хорошо, ведь это позволит избежать ошибок в работе приложения.

### Введение в DevOps и CI/CD

DevOps — это методология, которая объединяет разработку (Development) и эксплуатацию (Operations) для улучшения сотрудничества и автоматизации процессов в жизненном цикле программного обеспечения. Основная цель DevOps — ускорить доставку программного обеспечения, улучшить его качество и повысить удовлетворенность пользователей.

Одним из ключевых аспектов DevOps является внедрение процессов CI/CD (Continuous Integration/Continuous Deployment):

- **Непрерывная интеграция (CI)**: это практика, при которой разработчики регулярно интегрируют свои изменения в общий репозиторий. Каждый коммит автоматически тестируется, что позволяет быстро выявлять и исправлять ошибки.

- **Непрерывное развертывание (CD)**: это процесс автоматического развертывания изменений в производственной среде после успешного прохождения всех тестов. Это позволяет быстро и безопасно доставлять новые функции и исправления пользователям.

Внедрение DevOps и CI/CD помогает командам быстрее реагировать на изменения, улучшать качество программного обеспечения
и снижать риски, связанные с развертыванием.

### Введение в коды ответов HTTP

Коды ответов HTTP — это стандартные коды состояния, которые сервер возвращает в ответ на запрос клиента. Они помогают понять, как сервер обработал запрос. Вот некоторые из наиболее часто используемых кодов:

- **200 OK**: запрос был успешно обработан, и сервер вернул запрашиваемый ресурс.
- **201 Created**: запрос был успешным, и в результате был создан новый ресурс.
- **400 Bad Request**: сервер не может обработать запрос из-за ошибки клиента (например, неверный синтаксис).
- **401 Unauthorized**: для доступа к ресурсу требуется аутентификация.
- **404 Not Found**: запрашиваемый ресурс не найден на сервере.
- **500 Internal Server Error**: сервер столкнулся с ошибкой и не может обработать запрос.

Понимание этих кодов помогает разработчикам и тестировщикам быстро диагностировать и исправлять проблемы в приложениях.

### Статический и динамический анализ кода

Анализ кода — это процесс проверки исходного кода для выявления ошибок, уязвимостей и улучшения качества кода.
Существует два основных типа анализа кода: статический и динамический.

- **Статический анализ кода**: выполняется без запуска программы. Он анализирует исходный код на наличие ошибок, уязвимостей и несоответствий стилю кодирования.

- **Динамический анализ кода**: выполняется во время выполнения программы. Он помогает выявлять ошибки, которые могут возникнуть только при определенных условиях выполнения.

Использование обоих типов анализа помогает разработчикам создавать более надежное и безопасное программное обеспечение.

### Теория юнит-тестирования

Юнит-тестирование — это метод тестирования программного обеспечения, при котором отдельные модули или компоненты программы проверяются на корректность работы. Основная цель юнит-тестирования — убедиться, что каждый модуль работает правильно в изоляции от других частей системы.

- **Как писать юнит-тесты**:
    1. **Выбери модуль или функцию** для тестирования.
    2. **Определи ожидаемое поведение**: что функция должна делать при определенных входных данных.
    3. **Напиши тест**: создайте тестовый случай, который проверяет, соответствует ли фактический результат ожидаемому.
    4. **Запусти тест**: убедитесь, что тест проходит успешно. Если нет, исправьте код или тест.

Юнит-тестирование является важной частью процесса разработки, так как оно помогает поддерживать качество и надежность программного обеспечения.

## Chapter III

❗ _Ты можешь скопировать свои приложения из предыдущего проекта и продолжать работу над ним или взять уже готовое. Положи их в директорию src. Понадобятся и django-, и react-приложения._

### Задание 1. Написание юнит‑тестов для Django‑приложения

Юнит-тестирование — это проверка отдельных блоков кода в изоляции. Эти тесты повышают надежность системы и упрощают внесение изменений в код.

1. Установи зависимости для тестирования — `pytest` и `pytest-django`.
2. Создай файл `pytest.ini` в корне проекта (на одном уровне с `manage.py`).
3. В нем опиши `DJANGO_SETTINGS_MODULE` и `python_files`.
4. Создай файл с тестом моделей: `appointments/tests/test_models.py` и проверь:
    - автоматическую генерацию возраста пациента;
    - создание доктора.

Для работы с тестовыми методами тебе нужно сделать объект и при помощи `assert` проверить, что значения совпадают с ожидаемыми.

### Задание 2. Функциональное тестирование API

Функциональное тестирование — направлено на проверку корректности работы функциональности приложения. Напиши тесты для API:

1. Сделай файл `appointments/tests/test_api.py`.
2. Напиши тест для проверки создания встречи:
    - опиши данные запроса;
    - отправь запрос на `API`;
    - проверь, что код ответа `201`;
    - проверь совпадение данных встречи, которая была создана в БД, на соответствие отправленным данным.
3. Напиши тест для регистрации пациента:
    - опиши данные запроса (но не указывай `birth_date`, который является обязательным);
    - отправь запрос на `API`;
    - проверь, что код ответа `400`;
    - проверь, что пользователь и пациент не были созданы;
    - исправь код, если пользователь или пациент были созданы.

### Задание 3. Настройка линтера для Django‑проекта

Если ты пишешь код для себя, то можешь использовать любую структуру, главное — чтобы тебе было понятно, что он делает. Однако когда работаешь в команде, необходимо договориться о едином стиле. Например, можно установить правила форматирования кода, определить, использовать ли табуляцию или пробелы (а если пробелы, то сколько именно), решить, можно ли прямо вставлять числа в формулы или стоит применять только константы и переменные, а также согласовать, каким образом объявлять классы и работать с методами.

Чтобы эти стандарты соблюдались, нужен контроль: можно назначить ответственного программиста (что очень дорого и в плане времени, и в плане бюджета), проводить взаимное ревью кода (что не исключает человеческой ошибки) или доверить эту задачу линтеру.

У Django есть неплохой фреймворк-линтер, пришло время добавить его в проект и настроить:

1. Установи зависимость `flake8`.
2. Создай файл настроек `.flake8` в корне проекта.
3. Добавь эти настройки (посмотри доступные, может, какие-то еще захочешь добавить):

    ```markdown
    [flake8]
    max-line-length = 120
    exclude = .git,__pycache__,migrations,venv
    import-order-style = google
    application-import-names = appointments
    docstring-convention = google
    max-complexity = 10
    ```

4. Запусти `flake8`, посмотри, какие он нашел ошибки, и исправь их.

### Задание 4. Добавление логирования в Django‑приложение

1. В файле `hospital_project/settings.py` настрой логирование.
2. Для этого в `LOGGING = { ... }` добавь такие параметры, как `formatters`, `handlers`, `root`. Посмотри примеры лучших практик и опции, которые нужно указать.

    [Примеры лучших практик логирования в Django.](https://docs.djangoproject.com/en/stable/topics/logging/)

3. Добавь во всех `views.py` логирование, как минимум:

    ```python
    def some_view(request):
        logger.info("Начало выполнения some_view")
    ```

### Задание 5. Добавление кеширования в Django‑приложение

Кеширование — это процесс сохранения часто используемых данных в быстром хранилище, что позволяет при повторных запросах возвращать их без обращения к основному источнику (например, к базе данных или внешнему сервису). Это существенно ускоряет обработку запросов и снижает нагрузку на сервер.

Например, есть справочник с информацией code — name. На фронте нам нужно для каждого code получать name. Получается постоянная работа с БД (возможно, еще и через другой сервис — например, сервис справочников). Если мы имеем гарантию, что справочник не меняется (или меняется редко), мы можем быть довольны кешем с временным хранилищем — например, на сутки. Есть и другие способы, например, обновление кеша при обновлении справочника, о них ты можешь почитать — в работе программиста эта задача встречается довольно часто.

1. В `hospital_project/settings.py` настрой кеширование с помощью `LocMemCache`.
2. В представлении, например, для списка кабинетов, добавь кеширование (скажем, кешировать 5 минут).
3. Убедись, что данные списка кабинетов не изменяются (например, переименуй кабинет).

### Задание 6. Тестирование React‑компонентов

Сделай также тестирование на фронте — при помощи библиотек `Jest` и `React Testing Library`.

1. Создай файл `src/__mocks__/react-router-dom.js`. В нем опиши мок:

    ```js
    import React from 'react';
    
    const BrowserRouter = ({children}) => <div>{children}</div>;
    const Routes = ({children}) => <>{children}</>;
    const Route = ({element}) => element;
    const Link = ({to, children, ...props}) => <a href={to} {...props}>{children}</a>;
    
    export {BrowserRouter, Routes, Route, Link};
    export default {
        BrowserRouter,
        Routes,
        Route,
        Link,
    };
    ```

    _Этот мок представляет собой простой, часто минимальный вариант реализации (stub) модуля, который не вызывает проблем с трансформацией или синтаксисом. Без этого мока Jest пытается импортировать оригинальный пакет react-router-dom, который может использовать синтаксис ES-модулей, не обрабатываемый корректно в текущей конфигурации Jest._

2. Создай файл `src/__tests__/DoctorList.test.js`.
3. В нем сделай мок отображения списка врачей. Сделай массив с врачом, отрендери и сделай ожидание появления имени врача.
4. Запусти тест и проверь успешное выполнение.

### Задание 7. Настройка ESLint и исправление ошибок линтера

Линтер существует и для фронт-разработки тоже. :) Ты уже знаком с идеей и принципом:

1. Установи зависимость `eslint`.
2. Инициализируй конфигурацию ESLint (например, выбери React, JavaScript modules, Browser и т. д.).
3. Пример файла `.eslintrc.json`:

    ```json
    {
      "env": {
        "browser": true,
        "es2021": true,
        "jest": true
      },
      "extends": [
        "react-app",
        "plugin:react/recommended",
        "airbnb"
      ],
      "parserOptions": {
        "ecmaFeatures": {
          "jsx": true
        },
        "ecmaVersion": 12,
        "sourceType": "module"
      },
      "plugins": [
        "react"
      ],
      "rules": {
        "react/jsx-filename-extension": [
          1,
          {
            "extensions": [
              ".js",
              ".jsx"
            ]
          }
        ]
      }
    }
    ```

4. Запусти линтер, исправь найденные ошибки и предупреждения.

Тестирование и оптимизация — неотъемлемая часть работы разработчика. Не так сложно написать ПО, как отладить и оптимизировать его. :) Не переживай, если тут возникли трудности, этот навык будет совершенствоваться всегда!

---

Ты устало откинулся на спинку стула и выдохнул. Теперь, кажется, все должно было работать и запускаться без ошибок. По крайней мере, ты на это надеялся. В Лаборатории больше никого не было — все твои коллеги спокойно отдыхали дома, и гудел только твой компьютер. Это немного удручало, но ты был рад, что быстро справился с проблемой. 

Кстати о еще одной проблемке... Ты посмотрел на закрытый кабинет Главврача. Сейчас в Лаборатории, кроме тебя, никого не было, так что ты мог бы... так сказать, проверить свои догадки. 

Ты поднялся и подошел к двери, вежливо постучав. Разумеется, тебе никто не ответил, тогда ты с чувством выполненного долга нажал на ручку и зашел внутрь. Ты уже тут бывал, но сегодня хотел проверить вполне определенную вещь: ряд фотографий на столе Главврача. Крадучись ты зашел в темный кабинет, включил свет, обогнул стол и внимательно посмотрел на рамки. 

На одной был Главврач с какой-то женщиной, возможно, его женой, на другой — взрослая девушка (возможно, дочь), но тебя заинтересовало не это. А групповой снимок, кажется, изображавший большую семью. И вот оно: в заднем ряду Главврач премило беседовал с Вениамином, а на переднем плане Кларисса, присев на корточки, обнимала сына! Они и правда были знакомы! Более того, они, кажется, были родственниками! Но что все это могло значить?

Пока ты разглядывал фотографию, твой телефон в кармане завибрировал. Даже еще не достав его, ты знал, кто это может быть. 

>Вернусь уже завтра! Жди меня, только очень жди! 
>>**СМС от Главврача**

«Да кто вообще вас ждет», — подумал ты, ставя рамку обратно на стол. С другой стороны, пусть объяснит, какого черта ты горбатишься на его родственников, которых он сплавил, а сам куда-то свинтил. Ты выключил свет и вышел, не заметив, как к двери медленно повернулась камера видеонаблюдения. 

---

💡 [Нажми сюда](https://oprosso.ru/p/ad3bc98eb2a54c0baf4679fa722b54df), **чтобы поделиться с нами обратной связью на этот проект**. Это анонимно и поможет команде Продукта сделать твое обучение лучше.