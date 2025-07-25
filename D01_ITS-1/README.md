# Основные инструменты разработчика

## Аннотация

Данный проект позволит тебе познакомиться с такими основными инструментами разработчика, как командная оболочка bash, система контроля версий Git,
система управления репозиториями GitLab и среда разработки PyCharm.

## Содержание

1. [Chapter I](#chapter-i) \
    1.1. [Рекомендации к проекту](#рекомендации-к-проекту) \
    1.2. [Введение](#введение)
2. [Chapter II](#chapter-ii) \
    2.1. [Инструкция от админа](#инструкция-от-админа) \
    2.2. [Задание 1](#задание-1) \
    2.3. [Задание 2](#задание-2) \
    2.4. [Задание 3](#задание-3)
3. [Chapter III](#chapter-iii) \
    3.1. [GitLab](#gitlab) \
    3.2. [SSH-ключ](#ssh-ключ) \
    3.3. [Задание 4](#задание-4) \
    3.4. [Задание 5](#задание-5)
4. [Chapter IV](#chapter-iv) \
    4.1. [PyCharm](#pycharm) \
    4.2. [Задание 6](#задание-6) \
    4.3. [Задание 7](#задание-7) \
    4.4. [Задание 8](#задание-8)
5. [Chapter V](#chapter-v)

## Chapter I

### Рекомендации к проекту

Привет, студент! \
Рады приветствовать тебя на нашем интенсиве по языку Python. 

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

> Привет, стажер! Добро пожаловать в городскую поликлинику №13 города Средние Чебурки!
> Я слышал, как ты помог в регистратуре починить принтер. Молодец, хвалю! Похоже, ваш медвуз не только врачей, но и айтишников готовит.
>> **Главврач**

> Но... я просто перезагрузил его. Я не айтишн...
>> **Стажер**

> Не скромничай! Приятно видеть, что молодое поколение не кичится своими умениями. 
> Ну раз айтишник, то будешь помогать нашей поликлинике в цифровизации. 
> В областном центре вон, говорят, уже карточки пациентов перевели в электронный вид.
> А в Москве так вообще в электронную очередь по телефону записывает робот!
> До чего техника дошла! Пора и нам цифровизоваться!
>> **Главврач**

> ...
>> **Стажер**

> В ординаторской как раз компьютер стоит. Им раньше наш админ пользовался, но, к сожалению, он от нас ушел.
> Говорят, решил свою квалификацию поднять и в какую-то «Школу 21» поступил. Странно, вроде он уже закончил все 11 классов... Ну да ладно, о чем это я?
>> **Главврач** 

> Компьютер в ординаторской.
>> **Стажер** 

> Точно! Короче, админ наш перед уходом сказал, что оставит на этом компьютере какие-то инструкции для своего преемника.
> Так вот, твое первое задание на стажировку — ознакомиться с инструкциями! Порыскай по папкам, может, найдешь что полезное!
>> **Главврач**  

> А как же задания, связанные с медици...
>> **Стажер**  

> Спасибо и пока, у меня полно работы!
>> **Главврач**   

Главврач не дает тебе договорить, разворачивается и уходит по своим делам, оставляя тебя в полном недоумении...

## Chapter II

### Инструкция от админа

Ты доходишь до ординаторской, и местные врачи указывают тебе на добротный компьютер, стоящий в углу.
Ты включаешь его и не видишь знакомой иконки Windows при запуске. Ты видишь незнакомую надпись, возможно, название операционной системы и вспоминаешь, что главврач перед уходом остановился и бросил еще одну фразу:

> Ах да, чуть не забыл, у нас на компьютерах стоит **Linux** вместо Windows, не удивляйся. Импортозамещение, сам понимаешь.
>> **Главврач**

Ты видишь вполне себе похожий на винду рабочий стол, и на нем особенно выделяется файл, который называется *ReadMeeeeeeeeeeee!!!!!!.txt*.
В нем ты видишь следующую информацию:

> Привет, сменщик! \
> Ставлю сотку, что ты не айтишник. Откуда я догадался? Потому что сам я был уборщиком, но стоило мне один раз перезагрузить принтер главврачу, и все...
> Не успел я оглянуться, как сижу за этим компом и разбираюсь в премудростях айти... 
> 
> Для начала тебе, как и мне в свое время, нужно разобраться с такой вещью, как **терминал**. Что такое терминал, спросишь ты? 
> Видел в фильмах черный экран, где хаЦкеры как не в себя пишут какой-то код? Забудь об этом. Из правды там только черный экран
> и то, что туда надо что-то писать.
> 
> Когда-то давно у компьютеров не было графической оболочки. Никаких рабочих столов и иконочек на нем. Ты запускал компьютер и видел
> этот черный экран с мигающим курсором. И все действия — создание файлов и папок, переименование, копирование и миллион других
> привычных тебе действий — надо было писать через терминал. Хоть графический интерфейс и появился уже сто лет назад, но на любой
> операционной системе, включая винду, все же стоит терминал. И разные разработчики действительно продолжают постоянно им пользоваться.
> 
> А теперь я открою тебе еще более страшную тайну. Огромное количество компьютеров на Земле — это так называемые серверы (например, там обычно располагают сайты),
> на которых нет графического интерфейса, и разработчики, как в старые добрые доисторические времена, работают с ними через терминал.
> Да и, честно говоря, некоторые даже стандартные операции а-ля копирование проще иногда сделать через терминал. Ну вот, например,
> есть у тебя папка с тысячами файлов с разными расширениями. И тебе нужно скопировать в другую папку только картинки (то есть расширения
> png и jpeg, допустим). Ну вот попробуй это сделать мышкой через графические папочки для тысяч картинок. Как говорится — удачи. А через терминал это займет всего ничего.

### Задание 1

> **Терминал** — это программа, дающая доступ к **командной оболочке**, которая выполняет команды, вводимые человеком в терминал.
> То бишь, терминал — это сама программа, куда ты текстом пишешь команды. Под капотом этого терминала есть командная оболочка,
> которая исполняет эти команды. Командные оболочки бывают разными, одной из самых распространенных является **bash**, который
> и стоит на этом компьютере.
> 
> Этот bash позволяет делать то же самое, что ты делаешь на винде с помощью мышки: смотреть папки, копировать, перемещать, удалять файлы и папки, проваливаться в них и т. д. Думаю, идею ты понял.
> Но делается это через ввод специальных команд в терминал.
> 
> Попробуй посмотреть через терминал, где ты находишься — в какой папке. Не забудь разобраться, что означает этот путь! Ну и в целом — осмотрись, посмотри, что находится в **корневой папке**,
> в **домашней папке пользователя** и папке **/home/**.
> 
> Кстати, хочу предупредить тебя. Если это твой первый день, то, скорее всего, в конце дня главврач попросит тебя продемонстрировать
> все выполненные тобой терминальные команды за день. Так что либо запомни их, либо запиши куда-нибудь.

Итого, что тебе нужно сделать:
1. Понять, как запустить терминал на компьютере.
2. Определить, с помощью какой команды через терминал узнать, в какой папке ты находишься. И какой путь до этой папки.
3. Было бы неплохо погуглить, как устроена файловая система в Linux, откуда начинаются все пути и какие пути вообще бывают.
4. Посмотреть, что еще находится на этом компьютере. Необходимо перейти в следующие папки и посмотреть, какие файлы в них находятся:
    - корневая папка;
    - домашняя папка пользователя;
    - папка /home/.

   И, естественно, все это нужно сделать с помощью команд для bash.
5. Записать себе все команды и их последовательность для будущей быстрой демонстрации другому человеку.


### Задание 2

Ты возвращаешься к инструкции:

> Отлично, время создать папку, в которой ты будешь хранить все проекты. Назови ее, пожалуйста, *projects* и создай внутри своей **домашней папки**.
> 
> Думаю, что самое время заодно потренироваться создавать не только папки, но и файлы, а также научиться писать в них текст.
> Советую сделать следующее:
> 1. Создать два файла.
> 2. Открыть их через текстовый редактор в терминале и написать какой-нибудь текст.
> 3. Сохранить написанное и закрыть файл.
> 4. Прочитать содержимое файлов с помощью команды `cat`, чтобы убедиться, что текст сохранился.
> 
> Естественно, все операции нужно проделать командами **bash** через **терминал**.
> 
> P.S. У нас в терминале стоит два текстовых редактора — **nano** и **vim**. Воспользуйся одним из них для написания текста.
> Но хочу тебя предупредить! Vim не для слабонервных! Говорят, что каждый может открыть его, но далеко не каждый способен туда что-то написать, а тем более
> сохранить и выйти из него! Если тебе дороги твои нервы — воспользуйся nano. Если же ты любишь острые ощущения, то 
> vim, несомненно, тебе их доставит.

Итак, ты понимаешь, что нужно через терминал:
1. Создать папку *projects* в **домашней папке**.
2. Внутри папки *projects* создать два текстовых файлов — *test_file_1.txt* и *test_file_2.txt*.
3. Используя nano или vim, по очереди открыть эти файлы. В файле *test_file_1.txt* написать фразу: `I am a future programmer`.
В файле *test_file_2.txt* написать фразу: `I just fixed the printer...`.
4. Сохранить написанное в файлах и выйти из текстового редактора.
5. Проверить содержимое файлов с помощью команды `cat`.
6. Записать себе все команды и их последовательность для будущей быстрой демонстрации другому человеку.

### Задание 3

> По моему опыту, главврач любит еще спрашивать про базовые операции с файлами и папками — копирование, переименование, удаление.
> Советую тебе научиться ими пользоваться, например, проделав следующие действия:
> 1. Создай папку *folder* в **домашней папке**.
> 2. Скопируй туда файлы *test_file_1.txt* и *test_file_2.txt*.
> 3. Переименуй их.
> 4. Удали папку *folder* вместе с содержимым.

Ты составляешь чуть более подробный план действий, а именно:
1. Создать папку *folder* в **домашней папке**.
2. Скопировать в папку *folder* файлы *test_file_1.txt* и *test_file_2.txt* из папки **projects**.
3. В папке *folder* переименовать их в *test_file_1_copy.txt* и *test_file_2_copy.txt*.
4. Проверить с помощью команды `cat` их содержимое и убедиться в наличии текстов.
5. Удалить папку *folder* вместе с файлами *test_file_1_copy.txt* и *test_file_2_copy.txt* с помощью одной команды (ты уверен,
что такая команда есть).
6. Вывести в терминал содержимое домашней папки и убедиться, что папка *folder* отсутствует.
7. Записать себе все команды и их последовательность для будущей быстрой демонстрации другому человеку.

## Chapter III

### GitLab

Пока идет вполне себе неплохо, возможно, тебе даже нравится? Хм, пока еще явно рано об этом говорить.
Пора вернуться к инструкции.

> Итак, надо подсветить тебе некоторые моменты, связанные с программной инфраструктурой этой поликлиники. \
> Для нашей поликлиники город развернул специальную платформу — **GitLab**. Эта платформа позволяет:
> 1. Хранить твой код.
> 2. Сохранять историю всех изменений в коде и быстро возвращаться к любым старым версиям. Это называется **контроль версий**.
> Это гораздо более продвинутая версия старой доброй системы папок с названиями — *версия_1*, *версия_2*, *финальная_версия* и *финальная_финальная_версия* (шучу, это работает, конечно, сложнее, но зачем это нужно, я думаю, ты понял).
> 3. Работать в команде с другими разработчиками, т. е. организовывать совместную разработку.
> 
> На самом деле, GitLab имеет гораздо больше функций, но эти 3 самые основные. Пока что тебе их должно быть достаточно.
> Помимо GitLab, существуют и другие платформы с похожими функциями. Например, **GitHub** или  **BitBucket**. Но у нас 
> используется GitLab, с ним и будем работать.
> 
> На самом деле, все эти вышеперечисленные платформы построены на системе управления версиями **Git**. Вот по этой [ссылке](https://git-scm.com/book/ru/v2) ты найдешь отличный
> самоучитель по гиту. Советую тебе прочитать для начала главы 1.1, 1.3, 1.4 и 1.7.
> 
> Git уже установлен на этом компьютере, так что ставить его еще раз не нужно. В терминале должны быть доступны его команды.

### SSH-ключ

> В нашем GitLab уже подготовлено определенное количество шаблонов под проекты. 
> Однако перед тем как начать работать с GitLab, необходимо настроить подключение этого компьютера к платформе (боюсь, мое уже устарело
> или было удалено). Советую тебе сделать это через **ssh**. **ssh** — это такой инструмент, который позволяет безопасно подключаться
> к другому компьютеру, серверу или, в нашем случае, платформе GitLab.
> 
> Чтобы настроить такое подключение, тебе нужно **сгенерировать** на своем компьютере **ssh-ключи** через терминал, разобраться, в чем отличие
> двух созданных ключей между собой, и закинуть один из них (разберись, какой именно) в GitLab. Могу предложить ссылку
> на официальную [документацию](https://docs.gitlab.com/ee/user/ssh.html), либо можешь попробовать нагуглить русские материалы
> для понимания.
> 
> При генерации ключей используй алгоритм шифрования **RSA 4096** и сгенерируй их в папке по умолчанию (посмотри, что это за папка).
> Названия файлов советую тоже не менять, а оставить по умолчанию. Если вдруг данных алгоритм шифрования не будет работать,
> то можешь попробовать **RSA 256**.
> 
> Еще одна ремарка. Если будешь искать файлы с этими ключами через терминал (а иногда даже через графическую оболочку), то
> учти, что папки и файлы, которые начинаются на точку, являются **скрытыми**. Чтобы их видеть, обычно нужно дописывать в команды
> определенные **параметры**. 
> 
> И еще одна ремарка (на этот раз последняя). При генерации ключей тебе предложат ввести пароль. Он не будет отображаться в терминале — это фишка
> линуксов, не пугайся. Ввод работает, просто не отображается. Советую ввести такой пароль, который ты запомнишь. Тебе его еще потом часто 
> использовать, учти! Если же вдруг забудешь пароль, то сгенерируй новый ключ, а старый удали. Не забудь только переподложить
> его в гитлабе. Можно, кстати, просто нажать Enter вместо ввода пароля, и тогда пароль будет пустой (то есть его не будет), но так делать **категорически** не советую!
> Это небезопасно!

### Задание 4

Такс-с-с, получается, что тебе нужно сделать:
1. Сгенерировать ssh-ключи с помощью алгоритма RSA 4096 (что бы это ни было).
2. При генерации ключей путь до файлов и их имена оставить по умолчанию.
3. Ввести запоминающийся пароль для ключа.
4. Разобраться, какой из паролей и куда закинуть в GitLab, чтобы установить подключение между компьютером и платформой.

P.S. Если ключ с шифрованием RSA 4096 работать не будет, то можно удалить старые ключи и сгенерировать новые с шифрованием RSA 256.

### Задание 5

> Пора загрузить шаблон для первого проекта на свой компьютер. Попробуй **склонировать** (то есть скачать) **репозиторий** для
> первого проекта (*D01_ITS*) себе на компьютер в папку *projects*. Используй для этого ссылку для ssh и команду `git clone`.
> Можешь также прочитать [главу 2.5](https://git-scm.com/book/ru/v2/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git-%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D1%83%D0%B4%D0%B0%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8-%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F%D0%BC%D0%B8)
> в документации по гиту.
> 
> Проекты в гите также называются **репозиториями**. А репозитории на удаленных платформах а-ля GitLab — **удаленными репозиториями**.
> Не удивляйся, что внутри репозитория какие-то непонятные папки. Городские админы говорили мне, чтобы мы свой код писали в папке *src/* во всех проектах.
> Понятия не имею почему. 
> 
> Кстати, когда ты клонируешь проект, то устанавливается связь между удаленным репозиторием в GitLab и папкой с ним на твоем компьютере.
> Так что ты не просто качаешь его себе на компьютер!

Хм, кажется, ты понял следующее:
1. Нужно склонировать репозиторий *D01_ITS* на этот компьютер в папку *projects* с помощью ssh.
2. Проверить, что папка с репозиторием и его содержимым появилась на компьютере в папке *projects*.

## Chapter IV

### Ветвление в GitLab

Что там дальше?

> Надеюсь, что ты успешно склонировал свой первый репозиторий и, наверное, думаешь, что пора уже прогать. Но нет, перед тем как
> начать, ты должен узнать еще кое-что важное. Зайди в терминал, перейди внутри терминала в папку с репозиторием и напиши
> команду `git branch`. Видишь слово `master`? `master` — это **ветка** (или же **branch**). 
> 
> **Ветки** в гите — это параллельные версии проекта. Веток, как и версий, может быть очень много. Но главная ветка, на которой
> висит продакшн (это то, что уже юзают реальные пользователи), всегда одна. Она называется либо `master`, либо `main`, в зависимости от платформы. В этой ветке хранится
> самая главная, основная версия кода, которая доступна клиентам.
> 
> Давай на примере. Представь, что есть сайт нашей поликлиники. Сайт — это много кода, написанного на разных языках программирования. 
> Сами файлы с кодом, лежащим за последней работающей и оттестированной версией сайта (тот сайт, который ты видишь в браузере), лежат где-то в ветке `master`
> в репозитории для этого сайта в GitLab. Это грубый пример, но, надеюсь, стало немного понятнее.
> 
> А теперь представь, что на этот сайт нужно добавить новый функционал — например, поиск по врачам. Очень глупо будет
> заливать новый код для поиска в эту ветку `master`, ведь на ней и работает сайт, который виден пользователям. А если твой код с ошибками?
> Сайт просто упадет и не будет доступен пользователям. И это лишь сайт поликлиники. А теперь представь, если это банковское
> приложение или маркетплейс. За то время, что приложение или сайт будут недоступны, компания понесет огромные убытки.
> И все из-за ошибки в коде, которую принесли в ветку `master`.
> 
> Поэтому разработчики могут создавать другие ветки этого кода и в них безопасно добавлять новый код.
> Ветвление также помогает разработчикам разрабатывать несколько разных вещей одновременно, а потом соединять наработки в одной ветке,
> тестировать их и уже после заливать в главную ветку `master`.
> 
> Вот здесь можно подробнее почитать о **ветвлении**: <https://git-scm.com/book/ru/v2/Ветвление-в-Git-О-ветвлении-в-двух-словах>.
> 
> А здесь наглядный иллюстратор работы ветвления: <https://learngitbranching.js.org/?locale=ru_RU>.
> 
> К чему вся эта портянка текста ведет? К одному главному выводу. Писать код в ветке `master` — это ОЧЕНЬ плохо, и так делать нельзя.
> Для этого лучше создать отдельную ветку и писать свой код в ней. Советую тебе ВСЕ свои проекты реализовывать в ветке 
> `develop`, которая будет создана от ветки `master`.

### PyCharm

Кажется, получилось, что там дальше?

> Видимо, пора добавить немного кода в этот проект. На этом компьютере стоит программа, которую разработчики используют для написания кода.
> Найди ее, она называется **PyCharm Community Edition**. Это так называемая **IDE** или по-русски: интегрированная среда разработки.
> Вообще, код можно писать хоть в блокноте, но обычно для удобства используются специальные программы, такие как **PyCharm** или **Visual Studio Code**. \
> Попробуй открыть склонированный проект в PyCharm. В целом тебе нужно понять две главные вещи:
> 1. Главное окно посередине — это редактор, то есть пространство, где ты пишешь код.
> 2. Чтобы запустить код, который там будет написан, нужно подключить **интерпретатор** Python.
> 
> Что такое **интерпретатор**? Это программа, которая, собственно, считывает файлы с кодом и выполняет тот код, который написан
> внутри них. Я ведь уже говорил, что код можно писать хоть в блокноте, соблюдая определенный синтаксис и правила языка.
> А вот потом этот условный блокнот с кодом (правда, с расширением .py) скармливается интерпретатору, который выполняет код внутри.
> 
> То есть просто текст с кодом — это и есть язык программирования, иными словами, инструкции для компьютера, что надо делать.
> Так вот, интерпретатор считывает, анализирует и выполняет эти инструкции.
> 
> На компьютере уже стоит интерпретатор Python, однако тебе необходимо создать его копию для использования во всех своих будущих проектах. 
> И в каждом из них подключать эту единую копию. Этот интерпретатор сформируется внутри определенной виртуальной среды (или же виртуального окружения).
> Как его создать, я тебе сейчас расскажу.
> 
> Также я подготовил файл с библиотеками — *materials/requirements.txt*. Данные библиотеки могут пригодиться тебе в дальнейшем (что такое библиотеки, ты узнаешь чуть позже).
> Сразу установи их в этот новый интерпретатор.

### Задание 6

> Для того чтобы создать виртуальное окружение со своим интерпретатором и установить в него библиотеки, нужно:
> 1. Зайти в терминал.
> 2. Перейти в терминале в домашнюю папку своего пользователя (*/home/\<user>/*).
> 3. Прописать команду `python3 -m venv hospital_interpreter`.
> 4. Активировать виртуальную среду — `source hospital_interpreter/bin/activate`
> 5. Поставить в интерпретатор этой виртуальной среды библиотеки следующей командой — `pip3 install -r <путь до папки с 1 проектом>/materials/requirements.txt`
> 
> Теперь у тебя есть отдельный интерпретатор для всех проектов с необходимыми для них библиотеками.

### Задание 7

> Если моя догадка верна, и ты, как и я, делаешь свои первые шаги в программировании, то знай: у программистов есть традиция своим первым кодом писать: «Hello, something!».
> Поэтому, может, выведешь на экран: `Hello, IT!`? Можешь создать для этого новый питоновский файл *task_6.py*.
> 
> Не забудь, что все файлы с кодом надо создавать в папке *src/* и в отдельной ветке `develop`! Создать новую ветку
> и переключиться на нее можно как через терминал, так и через интерфейс PyCharm. Можешь выбрать любой удобный тебе способ.
> 
> Да, кстати, чтобы подключить уже существующий интерпретатор Python к проекту в PyCharm, тебе нужно будет указать путь до
> следующего файла в папке с этим интерпретатором — *<папка с интерпретатором>/bin/python*.

По-моему, количество информации растет слишком быстро... \
Ладно, что там в сухом остатке:
1. Нужно найти и открыть PyCharm.
2. Открыть в нем папку со склонированным репозиторием.
3. Через терминал или PyCharm создать новую ветку `develop` и переключиться на нее.
4. Подключить к проекту, созданный интерпретатор Python — **hospital_interpreter**.
5. Создать питоновский файл с названием *task_6.py* в папке *src/* внутри проекта.
6. Написать какой-то код, чтобы при выполнении программы на экран выводилась фраза `Hello, IT!`.

### Задание 8

Какая-то бесконечная инструкция...

> Теперь неплохо было бы залить свой код в **GitLab**. Для этого тебе нужно **закоммитить** и **запушить** те изменения, которые ты внес.
> Можешь для этого обратиться, опять же, к [инструкции гита](https://git-scm.com/book/ru/v2) к главам 2.2 и 2.5. Там на самом деле много
> ненужной для тебя сейчас информации, поэтому можешь попытаться загуглить сам, как залить изменения в GitLab, и что значат
> слова **закоммитить** и **запушить**. Все **коммиты** осуществляй в ветке `develop`. Пушить тебе также необходимо ветку
> `develop` в удаленный репозиторий в **GitLab**. 
> 
> P.S. Ты можешь выполнить эти операции как через PyCharm, так и через терминал. Через пайчарм проще и нагляднее, 
> а через терминал более трушно и хаЦкерно, но результат в итоге будет одинаков. Выбирай, что душе угодно.

То есть:
1. Нужно закоммитить и запушить новый файл с кодом *src/task_6.py* в GitLab в ветку `develop`.
2. Использовать для этого либо PyCharm, либо терминал.
3. Нужно проверить, что в удаленном репозитории *D01_ITS* на GitLab в ветке `develop` в папке *src/* лежит файл *task_6.py* с кодом.

## Chapter V

> Поздравляю тебя! Надеюсь, что у тебя все получилось, и твоя голова не кружится от обилия новой информации.
> На этом моя инструкция заканчивается. Однако я подозреваю, что тебе, возможно, понадобится еще кое-какая помощь в разных темах Python.
> Поэтому я взял на себя смелость и создал несколько файлов на разные темы Python, быть может, они направят тебя в нужное русло. \
> А теперь я наконец могу пожелать тебе удачи! В этой поликлинике очень дружелюбный и интересный персонал, думаю, ты не соскучишься. :) 

💡 [Нажми сюда](http://opros.so/gRcUp), **чтобы поделиться с нами обратной связью на этот проект**. Это анонимно и поможет команде Продукта сделать твоё обучение лучше.
