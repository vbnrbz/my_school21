# Функциональное программирование

## Аннотация

Данный проект позволит тебе подробнее изучить основы функционального программирования в Питоне. 

## Содержание

1. [Chapter I](#chapter-i) \
    1.1. [Рекомендации к проекту](#рекомендации-к-проекту) \
    1.2. [Введение](#введение)
2. [Chapter II](#chapter-ii) \
    2.1. [Задание 1](#задание-1)
3. [Chapter III](#chapter-iii) \
    3.1. [Функциональное программирование в Python](#функциональное-программирование-в-python) \
    3.2. [Задание 2](#задание-2) \
    3.3. [Задание 3](#задание-3) \
    3.4. [Задание 4](#задание-4) \
    3.5. [Задание 5](#задание-5) \
    3.6. [Задание 6](#задание-6) \
    3.7. [Задание 7](#задание-7)
4. [Chapter IV](#chapter-iv) \
    2.1. [Задание 8](#задание-8)

## Chapter I

### Рекомендации к проекту

Привет, студент! \
Рады приветствовать тебя на нашем интенсиве по языку Python. \

Как учиться в «Школе 21»:  
- На протяжении всего курса ты будешь самостоятельно добывать информацию. Пользуйся всеми доступными средствами поиска информации, к примеру, Google и GigaChat. Будь внимателен к источникам информации: проверяй, думай, анализируй, сравнивай. 
- Взаимообучение (P2P, Peer-to-Peer) — это процесс, при котором учащиеся обмениваются знаниями и опытом, выступая одновременно в роли учителей и учеников. Этот подход позволяет учиться не только у преподавателя, но и друг у друга, что способствует более глубокому пониманию материала.
- Не стесняйся просить помощи: вокруг тебя такие же пиры, которые тоже проходят этот путь впервые. Не бойся откликаться на просьбы о помощи. Твой опыт ценен и полезен, смело делись им с другими участниками. 
- Не списывай, а если пользуешься помощью — всегда разбирайся до конца, почему, как и зачем. Иначе твое обучение не будет иметь никакого смысла. 
- Если ты на чем-то застрял, и кажется, что ты уже все перепробовал, но все равно непонятно, куда идти, — просто передохни! Поверь, этот совет помогал многим разработчикам в их работе. Проветрись, перезагрузи голову и, возможно, в следующий раз тебе наконец придет нужное решение!
- Важен не только результат обучения, но и сам процесс. Нужно не просто решить задачу, а понять, КАК ее решить. 
- Следи за временем при выполнении проекта. В день ты должен преодолевать минимум одно испытание. 
- Помни, что каждое задание по завершении проекта проходит ряд проверок: р2р-проверка с помощью чек-листа, проверка набором автотестов, проверка на стиль кода, проверка статическим анализатором, проверка на корректную работу с памятью. 

Как работать с проектом: 
- Перед выполнением проект необходимо склонировать с GitLab в одноименный репозиторий.
- Все файлы с кодом необходимо создавать в папке src/ склонированного репозитория.
- После клонирования проекта необходимо создать ветку `develop` и вести разработку в ней. После этого пушить в GitLab также нужно ветку `develop`.
- В качестве интерпретатора Python для всех проектов необходимо использовать единый интерпретатор, который ты создал в 1 проекте — **hospital_interpreter**.
- В твоей директории не должно быть иных файлов, кроме тех, что обозначены в заданиях.
- **Жирным** шрифтом будут выделены слова, на которые тебе нужно будет обратить более пристальное внимание, не стесняйся их гуглить!
- *Курсивом* будут выделены имена папок и файлов, названия проектов и т. д.
- В таком блоке `a = 10 * 3` будут представлены куски кода или те строки, которые должны выводиться кодом.
- В такой блок <insert...> (отличается от верхнего скобками < >) нужно подставить что-то из твоего кода, возможно, какую-то переменную.
- Каждое задание необходимо выполнять в отдельном файле. Название должно содержать task_ и номер задания. Например, task_1.py, task_2.py и т. д. Если задание подразумевает создание дополнительных файлов, то их местоположение в папке src и названия будут прописаны в теле задания.
- Все пути к файлам в коде указывай просто в виде строки. Не используй для этого библиотеки по типу `pathlib`. Это необходимо для корректной работы автотестов!
- Выход из программы **НЕ ДОЛЖЕН** осуществляться с помощью метода `exit` или же `sys.exit()`. Это также необходимо для корректной работы автотестов!

Дисклеймер: 
- Наша команда не медики. Если ты будешь видеть в тексте медицинские неточности или ошибки, заранее просим у тебя прощения. Оставляй нам обратную связь, и мы все поправим!
- Иногда повествование ведется в несколько шутливой форме, чтобы не было скучно. Однако, как ты и сам знаешь, юмор и шутки — субъективная вещь. Поэтому если каламбуры в данном тексте, по твоему мнению, попахивают батиным юмором, то, пожалуйста, просто прими это.

Удачи тебе на этом тернистом, но определенно полезном пути!


### Введение

Ты сидишь, качаешься на стуле и думаешь о том, что пошла последняя неделя твоей практики. Интересно, насколько насыщенной она будет? В этот момент дверь со скрипом открылась, словно вселенная посылала тебе ответ. В виде главврача...

> Здравствуйте!
>> **Стажер**

> Hello, it's meee...
>> **Главврач, тихонько напевая мелодию**

> I was wooondering if after all these years                                     
> You’d like to meeeeet,                                                                           
> To go oooover everythiiiing.                                                                    
> They say that time’s supposed to heal ya,                                
> But I ain't done much healing...          
>> Вы вместе, но не очень громко

Кажется, две недели вместе дают о себе знать. Это даже немного пугает, честно говоря...

> Ты мне начинаешь нравиться все больше, стажер! Скажу честно, вообще-то, я шел мимо и даже больше, хотел на этой неделе не трогать тебя.
> Но твое страстное исполнение меня так задело, что я решил все-таки уделить тебе свое личное время на всю оставшуюся практику!
>> **Главврач**

> Да ёшки-матрёшки, кто меня за язык вообще тянул... Стоп. Какие еще «ёшки-матрёшки»?! Кажется, я начинаю психологически стареть 
> с каждой минутой!
>> **Стажер, думая про себя**

> Приятно видеть на твоем лице столько энтузиазма! Только мне нужно будет сейчас ненадолго отлучиться, давай я тебе дам
> задачку, и пока ты ее решаешь, закончу свои дела.
>> **Главврач**

## Chapter II

### Задание 1

> Задачка следующая. В новом проекте в файле *materials/number_of_visits.json* лежит статистика посещения
> пациентами нашей поликлиники за 4 месяца по двум врачам. Обращу твое внимание, что формат немного странный. Где-то указанно кол-во
> посещений в разрезе дней недели, где-то сразу за всю неделю, а где-то даже сразу за весь месяц.
> 
> Твоя задача — написать функцию, которая будет считать общее кол-во посещений. Но, как в анекдоте, есть один НЮАНС. Функция
> должна быть **рекурсивной** и принимать на вход 2 аргумента: прочитанный заранее из файла словарь и счетчик, который будет считывать общее количество.
> Учти, что функция должна быть универсальной. Это значит, что другой файл с посещениями может содержать немного другой формат: 
> других врачей, другие года, другие месяцы, другую разбивку. И у меня есть парочка таких файлов для проверки.
> 
> Вижу в твоих глазах немой вопрос: «Что такое **рекурсия** и **рекурсивная функция**?». А вот тут ты уже сам давай разбирайся.
> Сделай так, чтобы основная функция `main` принимала путь к файлу, а возвращала числом общее кол-во (сумму) посещений.  
>> **Главврач**

Опять все сам... Ладно, пора структурировать задачу:
1. В файле *src/task_1.py* необходимо реализовать функцию `main`, которая принимает путь к файлу. Внутри она считывает файл и вызывает рекурсивную функцию, передавая туда словарь с прочитанными данными и нулевым счетчиком. Функция должна возвращать целое число — сумму всех чисел внутри файла.
2. В файле *src/task_1.py* необходимо реализовать функцию `recursive_counter`, которая принимает два аргумента: словарь с прочитанными данными и счетчик чисел.
Функция должна быть рекурсивной и считать сумму всех чисел из конечных значений словаря любой структуры, которой будет ей передан.
Ключевой момент: функция должна быть рекурсивной. Функция должна возвращать целое число — сумму всех чисел внутри файла.
3. Необходимо также проставить аннотации везде, где можно их проставить.

## Chapter III

### Функциональное программирование в Python

> И вот он снова я. Могу выделить чуть больше времени и рассказать тебе о еще одном стиле программирования. В теме по ООП
> мы затрагивали разные стили программирования, тогда, собственно, мы и разбирали объектно-ориентированный стиль. Сегодня я хочу
> поговорить о **функциональном стиле программирования**.
> 
> Функциональное программирование, как можно догадаться, крутится вокруг функций и ставит их во главу угла. Однако не
> стоит воспринимать код, где просто много функций, как функциональное программирование.
> 
> Функциональное программирование — это, скорее, про подход: здесь функции больше понимаются как математическое понятие, а не просто
> как подпрограмма. Вкратце смысл такой: меньше конкретных инструкций, больше описаний через функции. Есть целые функциональные языки программирования, где функциональный стиль является основополагающим
> столпом языка. Пример таких языков — **Haskell** и **F#**. 
> 
> Полноценно разбирать, в чем заключается функциональный подход, мы не будем. Мы лишь поговорим о том, что подразумевают, когда
> говорят о функциональном стиле в Python. Ключевые базовые моменты следующие (остальное уже детали):
> 1. Функции можно воспринимать как обычные данные. То есть их можно присваивать переменным, передавать в другие функции
> в качестве аргументов.
> 2. Возможность использовать анонимные функции (или **lambda-функции**).
> 3. Использование рекурсии как еще одного инструмента наряду с циклами.
> 4. Использование популярных встроенных функций, которые могут принимать на вход другие функции (`map`, `filter` и `zip`).
>   
> Если с 3 пунктом, ты уже, надеюсь, разобрался, выполняя 1 задание, то вот остальные надо бы отработать.
>> **Главврач**

> А конкретной теории не будет? А то все это звучит слишком абстрактно!
>> **Стажер**

> Хе-хе-хе. А ты еще не понял мой подход? Я накидываю тебя ключевые слова для Гугла, а дальше ты сам. Помни, что умение
> находить новую информацию — это один из самых важных навыков в современном мире!
>> **Главврач**

### Задание 2

> Давай начнем с того, чтобы ты понял, как это вообще — передать функции в качестве аргумента другую функцию.
> 
> В файле *materials/patients.json* лежит список словарей с данными пациентов. Тебе нужно сделать следующее:
> 1. Написать 3 функции, каждая из которых принимает на вход один аргумент — ОДИН словарь с данными пациента (в файле список таких словарей), а возвращает обработанный каким-то образом переданный словарь. А именно:
>   1) Функция `anonymize_patient` удаляет фамилию, имя и отчество из словаря (ключ+значение), чтобы анонимизировать данные пациента.
>   2) Функция `change_blood_type` меняет группу крови с иностранного обозначения на применимый у нас (кто вообще записал изначально группу крови в таком виде?).
> Вот словарь для изменения:
>      ```
>      {
>          "O+": "I+",
>          "A+": "II+",
>          "B+": "III+",
>          "AB+": "IV+",
>          "O-": "I-",
>          "A-": "II-",
>          "B-": "III-",
>          "AB-": "IV-"
>      }
>      ```
>   3) Функция `change_type_age` приводит возраст из словаря к целочисленному типу данных (изначально возраст в виде строки).
> 2. Нужно написать функцию `process_patients`, которая принимает на вход два аргумента: функцию, с помощью которой необходимо обработать каждый словарь из списка, 
> и сам список словарей с данными пациентов. Функция должна возвращать список словарей, обработанных переданной
> функцией. При этом я хочу:
>   1) чтобы новый список формировался на копии переданного в функцию списка (чтобы не трогать изначальный список);
>   2) чтобы для формирования нового списка ты использовал **генератор списков** в Python (узнай что это). Полезно знать на будущее.
> На всякий пожарный скажу, что такие генераторы есть не только для списков, но и вообще для любых коллекций.
> 3. Написать функцию `main`, которая принимает на вход один аргумент — путь к файлу с данными пациентов. Внутри функции `main`
> должна последовательно три раза вызываться функция `process_patients`. В каждый из вызовов `process_patients` передается одна из трех написанных функций (из пункта 1) в следующем порядке:
> `anonymize_patient`, `change_blood_type` и `change_type_age` и список из файла. Функция `main` должна возвращать кортеж из результатов этих трех последовательных вызовов `process_patients`.
> То есть кортеж из трех списков с обработанными словарями.
>> **Главврач**

Фух, остается только не забыть, что данное задание надо выполнить в файле *src/task_2.py*. А также не забыть проставить везде
аннотации! Не зря же ты их изучал. Простановка аннотаций - дело опциональное для этого проекта, но крайне рекомендуемое! 

P.S. Все пути надо указывать от рабочей папки (которую надо не забыть установить в PyCharm как папку с репозиторием).
P.P.S. Так как внутри `process_patients` реализована работа с копией списка, то изначальный список никогда не меняется.

### Задание 3

> Отлично, молодец. А теперь вместо функции `process_patients` в функции `main` используй встроенную функцию `map`.
> Разберись, как она работает. Только не забудь в нее передавать копии прочитанного из файла списка (а не оригинальный список). Функцию
> `process_patients` удали из кода для этого задания.
> 
> Функция `main` продолжает принимать тот же аргумент и возвращать тот же кортеж из трех списков с обработанными словарями.
> Просто данные списки теперь должны быть получены с помощью `map`.
> 
> В данном задании не импортируй ничего из файла с заданием 2. Просто скопируй нужный код в файл с этим заданием.
>> **Главврач**

И код этот нужно реализовать в файле *src/task_3.py*. Напоминания про аннотации и пути также актуальны!

### Задание 4

> Я надеюсь, ты понял, что из себя представляет функция `map`. Пойдем дальше.
>
> Теперь предлагаю тебе:
> 1. Написать 3 функции, каждая из которых также принимает на вход один аргумент — ОДИН словарь с данными пациента (в файле список таких словарей), 
> а возвращает тот же словарь, если он соответствует определенному условию, **в противном случае функции должны возвращать `None`**. Функции следующие:
>   1) Функция `filter_by_man` возвращает тот же словарь, если пациент — мужчина.
>   2) Функция `filter_by_absence_illness` возвращает тот же словарь, если у пациента нет ни одного хронического заболевания.
>   3) Функция `filter_by_age` возвращает тот же словарь, если пациент строго меньше 50 лет.
> 2. Написать функцию `process_patients`, которая принимает на вход два аргумента: функцию, с помощью которой нужно отбирать словари, 
> и сам список словарей с данными пациентов. Функция должна возвращать список словарей, которые прошли фильтры внутри переданной функции.
> При этом необходимо исключить `None` из нового словаря. При этом я хочу, чтобы новый список также формировался на копии переданного в функцию списка.
> На всякий пожарный скажу, что такие генераторы есть не только для списков, но и вообще для любых коллекций.
> 3. Написать функцию `main`, которая принимает на вход один аргумент — путь к файлу с данными пациентов. Внутри функции
> должна три раза вызываться функция `process_patients`, в которую передаются три написанные функции (из пункта 1) в следующем порядке:
> `filter_by_man`, `filter_by_absence_illness` и `filter_by_age` и список из файла. Функция `main` должна возвращать кортеж из результатов этих трех вызовов.
> То есть кортеж из трех списков с обработанными словарями.
>> **Главврач**

Код нужно реализовать в файле *src/task_4.py*. Напоминания про аннотации и пути также актуальны!

### Задание 5

> А теперь давай проделаем то же самое, что и с функцией `map`, только чуть усложнив.
> 
> Я хочу, чтобы вместо функции `process_patients` ты использовал встроенную функцию `filter` (разберись, как она работает).
> А вместо трех функций — `filter_by_man`, `filter_by_absence_illness` и `filter_by_age` — использовал lambda-функции, которые
> ты на лету сразу будешь передавать в функцию `filter`.
> 
> То есть в коде нужно реализовать ТОЛЬКО функцию `main`, которая принимает тот же один аргумент (путь к файлу), а возвращает тот же кортеж, что
> и в прошлом задании. Проверь себя тем, что функция `main` из этого задания должна возвращать абсолютно то же самое, что и 
> в прошлом задании.
> 
> Не забудь в `filter` передавать глубокую копию списка.
>> **Главврач**

Код нужно реализовать в файле *src/task_5.py*. Напоминания про аннотации и пути также актуальны! Импортировать ничего из задания 4 не нужно!

### Задание 6

> Давай закрепим знания по lambda-функциям и заодно изучим (если ты еще вдруг не сталкивался) встроенную сортировку в Питоне.
> 
> Я хочу, чтобы ты реализовал функцию `main`, которая принимает все тот же путь к файлу. После чтения списка пациентов
> с помощью встроенной функции `sorted` нужно отсортировать этот список по возрасту пациентов. Начиная от самого большого возраста к самому маленькому
> (0 элементом отсортированного списка должен быть самый старший пациент, последним элементом — самый младший).
> Используй для сортировки lambda-функцию (обрати внимание на параметр `key` у функции `sorted`).
> 
> После этого переназначь `ID` у каждого пациента согласно его месту в отсортированном списке. То есть у первого пациента в отсортированном списке `ID` должен
> стать 1 (НЕ 0, заметь!), у второго пациента по порядку `'ID': 2` и т. д. Можешь, кстати, для этого использовать функцию
> `enumerate`. Еще одна полезная функция, изучи, как она работает.
> 
> Функция `main` должна возвращать отсортированный по возрасту список с измененными айдишниками.
>> **Главврач**

Код нужно реализовать в файле *src/task_6.py*. Напоминания про аннотации и пути также актуальны!

### Задание 7

> Ну и последнее по порядку, но не по значению — это встроенная функция `zip`. Само собой, тебе нужно изучить эту функцию,
> а сделать надо следующее.
> 
> Необходимо реализовать функцию `main`, которая принимает все тот же путь к файлу. Внутри нужно объявить два списка:
> ```python
> keys = ['ID', 'Name', 'Surname', 'Patronymic', 'Age', 'Sex', 'Blood group', 'Chronic diseases']
> values = [11, 'Vasiliy', 'Vasiliev', 'Vasilievich', '48', 'Man', 'O-', ['Haemorrhoids']]
> ```
> С помощью функции `zip` сделать из них словарь, который надо добавить в общий список пациентов.
> 
> Функция `main` должна вернуть список пациентов, куда добавлен новый пациент (словарь).
>> **Главврач**

Код нужно реализовать в файле *src/task_7.py*. Напоминания про аннотации и пути также актуальны!

## Chapter IV

### Задание 8

> То, что ты сегодня узнал, конечно, не сильно раскрыло тебе суть функционального программирования. 
> 
> Но факт в том, что когда говорят о функциональном программировании в Python, в большинстве своем подразумевают эти вещи,
> а особенно функции `map`, `filter`, `zip` и lambda-функции.
> 
> Ладно, ты сегодня хорошо поработал! Хвалю! Не забудь все запушить на гитлаб.
> А я пошел, до завтра!
>> **Главврач**

Сказать, что ты не понял, что вообще здесь произошло, — это ничего не сказать. Но факт остается фактом: пуш в GitLab никто не отменял.
Тебе остается запушить все наработки в GitLab в ветку `develop` (все файлы *.py* из папки *src/*).

---

💡 [Нажми сюда](http://opros.so/gRcUp), **чтобы поделиться с нами обратной связью на этот проект**. Это анонимно и поможет команде Продукта сделать твоё обучение лучше.
