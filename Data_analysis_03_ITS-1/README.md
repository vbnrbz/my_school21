# Анализ медицинских данных

Аннотация: Данный проект позволит тебе научиться работе с данными и библиотеками статистики и машинного обучения в Python. Ты разберешься со статистической проверкой гипотез, визуальным анализом данных и машинным обучением.

## Содержание
1. [Chapter I](#chapter-i) \
   1.1. [Рекомендации к проекту](#рекомендации-к-проекту)
2. [Chapter II](#chapter-ii) \
   2.1. [Описание проекта](#описание-проекта)
3. [Chapter III](#chapter-iii) \
   [Анализ клинического исследования](#анализ-клинического-исследования)\
   3.1. [Задание 1](#задание-1-подготовка-окружения-и-знакомство-с-данными)\
   3.2. [Задание 2](#задание-2-визуальный-анализ)\
   3.3. [Задание 3](#задание-3-математическая-статистика-и-проверка-гипотезы)
4. [Chapter IV](#chapter-iv) \
   [Анализ данных о диабете](#анализ-данных-о-диабете)\
   4.1. [Задание 4](#задание-4-загрузка-и-исследование-данных)\
   4.2. [Задание 5](#задание-5-корреляционный-анализ)\
   4.3. [Задание 6](#задание-6-подготовка-данных-для-обучения-моделей)\
   4.4. [Задание 7](#задание-7-построение-и-оценка-базовой-модели-логистической-регрессии)\
   4.5. [Бонусное задание 8](#бонусное-задание-8-подбор-гиперпараметров-с-использованием-grid-search)


## Введение 
День начался великолепно: ты сидишь в университетском кафе, наслаждаешься вкусным кофе и круассаном, чтобы еще сильнее взбодриться в этой насыщенной жизни. Как вдруг после тебя поглощает дневной десятиминутный сон.\
И вот ты идешь по коридору огромной лаборатории, где представлены все самые последние инновационные медицинские технологии, останавливаешься у экспоната симулятора и видишь свою фамилию в списке, кто внес большой вклад в исследовании.

>Здравствуй, коллега! Рад тебя видеть в этих стенах, заходи почаще. Мне радостно наблюдать за твоими успехами! Ты определенно мой кринж, крип, гринч…
>>**Главврач**

>Уверен, что краш. 
>>**Стажер**

И тут сон обрывается, ты открываешь глаза и видишь перед собой главврача… 

>Привет, стажер! Как жизнь молодая, студенческая? Вижу, восполняешь силы, это прекрасно. Получил решения твоих первых проектов по клиническим исследованиям, и хочу сказать, что выглядит это весьма успешно. У меня для тебя будет еще один проект в этой области. Наша кафедра ценит твой вклад, и это помогает нам продвинуться в исследованиях. Для тебя, уверен, это тоже колоссальный опыт. 
>>**Главврач**

>О да, как ожидаемо приятно, сказать, что не готов, значит соврать. Так что жду с нетерпением чего-то нового!
>> **Стажер**

>Тогда смотри, основная цель нового проекта — провести анализ данных клинических исследований, убедиться в достоверности полученных результатов, оценить статистическую значимость и сделать выводы. Затем провести анализ данных пациентов с диабетом, выявить корреляции между признаками, построить модель машинного обучения для прогнозирования диабета и проверить её качество.\
>Как обычно, все подробности пришлю на почту.\
>Удачи!
>>**Главврач**

## Chapter I
### Рекомендации к проекту
Как учиться в «Школе 21»:  
- На протяжении всего курса ты будешь самостоятельно добывать информацию. Пользуйся всеми доступными средствами поиска информации, к примеру, Google и GigaChat. Будь внимателен к источникам информации: проверяй, думай, анализируй, сравнивай. 
- Взаимообучение (P2P, Peer-to-Peer) — это процесс, при котором учащиеся обмениваются знаниями и опытом, выступая одновременно в роли учителей и учеников. Этот подход позволяет учиться не только у преподавателя, но и друг у друга, что способствует более глубокому пониманию материала.
- Не стесняйся просить помощи: вокруг тебя такие же пиры, которые тоже проходят этот путь впервые. Не бойся откликаться на просьбы о помощи. Твой опыт ценен и полезен, смело делись им с другими участниками. 
- Не списывай, а если пользуешься помощью — всегда разбирайся до конца, почему, как и зачем. Иначе твое обучение не будет иметь никакого смысла. 
- Если ты на чем-то застрял, и кажется, что ты уже все перепробовал, но все равно непонятно, куда идти, — просто передохни! Поверь, этот совет помогал многим разработчикам в их работе. Проветрись, перезагрузи голову и, возможно, в следующий раз тебе наконец придет нужное решение!
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

### Описание проекта

Основная цель проекта — провести анализ данных клинических исследований, убедиться в достоверности полученных результатов, оценить статистическую значимость и сделать выводы. Затем провести анализ данных пациентов с диабетом, выявить корреляции между признаками, построить модель машинного обучения для прогнозирования диабета и проверить её качество.

Ты будешь работать с двумя наборами данных:

1.	Клиническое исследование вымышленного препарата: синтетические данные для оценки эффективности препарата по сравнению с плацебо.
2.	Данные о диабете: реальный датасет с информацией о женщинах старше 21 года, включающий различные медицинские показатели и наличие или отсутствие диабета.

Для работы рекомендуется использовать Jupyter Notebook, это очень удобное средство для работы с данными, кодом и визуализацией. Изучи, как можно установить Jupyter Notebook.
Рекомендуемый материал по установке — https://docs.jupyter.org/en/latest/install/notebook-classic.html#alternative-for-experienced-python-users-installing-jupyter-with-pip.
В данном случае Jupyter устанавливается как библиотека и вызывается как команда:
```
jupyter notebook
```

## Chapter III

### Анализ клинического исследования

### Задание 1. Подготовка окружения и знакомство с данными

Первым делом необходимо настроить окружение для работы:
* Установи библиотеки: numpy, pandas, matplotlib, seaborn, scipy, statsmodels, jupyter.
* Запусти Jupyter `jupyter notebook`, создай новый ноутбук в папке `src`.
* Создай новый Jupyter Notebook в `src/task1_clinical_trial_analysis.ipynb`.
* Загрузи датасет клинического исследования из файла `clinical_trial_data.csv` (файл предоставляется в `src`).

Все необходимые действия разбивай на ячейки в ноутбуке, оставляй побольше текстовых описаний перед ячейками. Для описания используй тип ячейки markdown, а для кода — code.

В начале тетрадки `task1_clinical_trial_analysis.ipynb` напиши оглавление `# Анализ медицинских данных`. Далее, при выполнении конкретного задания, пиши перед заданием заголовок с его именем. Например, для первого задания `## Задание 1. Подготовка окружения и знакомство с данными`.
По мере выполнения заданий сохраняй весь код и вывод ячеек. По коду и выводу будет проверяться работа. Следи за чистотой и аккуратностью тетрадки. Учитывай, что ее будут проверять другие пиры. Постарайся оставлять побольше комментариев в специальных текстовых ячейках формата `markdown`.

Далее ознакомься с данными:
* Убедись, что данные загружаются корректно и все столбцы имеют правильные типы данных.
* Выведи первые несколько строк датасета (head()).
* Проверь информацию о данных (info()), типы данных и наличие пропущенных значений.
* Выведи описательные статистики (describe()).

В ячейке ниже опиши данные, с которыми предстоит работать — ячейки, что они означают, количество данных, и если видишь какие-то особенности, укажи их.

### Задание 2. Визуальный анализ

Исследуя клинические данные, твоя задача — проверить гипотезу о том, что препарат действительно улучшает самочувствие пациентов по сравнению с плацебо.

1. Раздели данные на группы: группа, принимающая препарат, и группа, принимающая плацебо.
2. Построй гистограммы и boxplot для визуальной оценки самочувствия в каждой группе.
3. Текстом в markdown опиши свои выводы на основе визуализации.

### Задание 3. Математическая статистика и проверка гипотезы

Далее, тебе предстоит использовать математические инструменты статистики. Все используемые статистические тесты можно найти в библиотеке `scipy`. Изучи документацию и используй необходимые по заданию тесты.\
Результаты каждого статистического теста необходимо вывести и интерпретировать словами, описать, для чего необходимо делать данный тест и о чем именно он говорит в контексте клинического исследования препарата.

1. Проверь гипотезу нормальности распределения: тест Шапиро — Уилка.
2. Проверь гомогенности дисперсий: тест Левена для проверки равенства дисперсий между группами.
3. Выбор и проведение статистического теста:
   - Если данные нормально распределены и дисперсии равны, используй t-тест для независимых выборок.
   - Если условия t-теста не выполняются, используй непараметрический тест Манна — Уитни.
4. Рассчитай p-value и сравни с уровнем значимости (возьмем α = 0.05).
5. Сделай вывод о наличии или отсутствии статистически значимой разницы между группами.
6. Оцени размера эффекта: вычисли коэффициент Коэна d для оценки размера эффекта.

Рекомендации:
* Не забудь проверить условия применения выбранных статистических тестов.
* Обсуди возможные причины, если разница не является статистически значимой.

## Chapter IV
### Анализ данных о диабете

Теперь, когда ты завершил анализ данных клинического исследования, твоя задача — провести анализ второго набора данных, содержащего информацию о пациентах с диабетом. Этот набор включает различные медицинские показатели женщин старше 21 года и используется для исследования взаимосвязей между признаками и для построения предиктивной модели диабета.

### Задание 4. Загрузка и исследование данных

Для начала подготовь окружение и загрузи датасет `diabetes.csv`, расположенный в папке `src`.

1. Создай новый Jupyter Notebook в `src/task2_diabetes_analysis.ipynb`.
2. Загрузи данные в DataFrame и выведи несколько первых строк (head()).
3. Проверь информацию о данных (info()) и типы столбцов, убедись, что все данные загружены корректно.
4. Выведи описательную статистику (describe()) для всех числовых признаков.
5. Проверь наличие пропущенных значений, которые могут потребовать обработки.
6. Опиши, какие данные содержатся в датасете, что означает каждый признак, и если видишь какие-то особенности или аномалии, укажи их.

Рекомендация: не забудь добавлять текстовые комментарии и интерпретировать выводы, полученные на каждом этапе, в markdown-ячейках для ясности.

### Задание 5. Корреляционный анализ

В этом шаге мы будем исследовать корреляции между признаками, чтобы лучше понять, как разные факторы могут быть связаны с наличием диабета.

1. Построй тепловую карту корреляций для всех числовых признаков с помощью библиотеки Seaborn (heatmap).
Для улучшения визуализации добавь аннотации с числовыми значениями корреляций.
2. Проанализируй, какие признаки наиболее коррелируют друг с другом и с целевым признаком (Outcome).
3. Построй парные графики (pairplot) для наиболее значимых признаков по результатам корреляционного анализа.
Например, выбери Glucose, BMI, Age и Outcome.
4. Для каждого важного признака, отдельно визуализируй распределения по группам (например, с помощью boxplot или violin plot) для пациентов с диабетом (Outcome=1) и без диабета (Outcome=0).
5. Опиши выводы по корреляционному анализу: какие признаки имеют сильную положительную или отрицательную корреляцию с наличием диабета. 
Напиши свою версию, почему признаки коррелируют или не коррелируют друг с другом.

Рекомендация: следи за цветовой схемой и четкостью визуализаций, чтобы легче было выделить различия между группами и делать выводы о данных.

### Задание 6. Подготовка данных для обучения моделей

В следующих заданиях тебе предстоит создать и обучить модель для прогнозирования диабета, используя алгоритмы машинного обучения.
Давай сосредоточимся на базовой модели — логистической регрессии, а также на подборе гиперпараметров для повышения её точности.

Перед началом обучения модели необходимо подготовить данные для построения прогнозов.

1. Выдели обучающие признаки — все, кроме Outcome, обозначь данные этого признака буквой X.
2. Выдели целевой признак — Outcome, обозначь буквой y.
3. Раздели данные на обучающую и тестовую выборки в соотношении 70/30. Обозначь данные X_train, X_test, y_train, y_test.
4. Проверь распределение целевого признака в обучающей и тестовой выборках, чтобы убедиться, что данные сбалансированы.
5. Масштабируй числовые признаки (например, с помощью StandardScaler из sklearn), чтобы улучшить работу модели.

### Задание 7. Построение и оценка базовой модели логистической регрессии

Теперь настало время построить простую модель и проверить её качество на тестовых данных.

1. Обучи модель логистической регрессии на обучающей выборке.
2. Сделай прогнозы на тестовой выборке и оцени точность модели с помощью следующих метрик:
   - Accuracy,
   - Precision и Recall,
   - F1-score,
   - ROC-AUC.
3. Качество модели должно быть в районе 75-95% по метрике Accuracy, если получилось иное значение — ищи ошибку.
4. Сделай выводы о качестве модели, насколько хорошо она предсказывает заболевание и насколько можно полагаться на нее.

Рекомендация: обязательно объясни, почему каждая метрика важна в контексте задачи прогнозирования диабета и как она интерпретируется.

### Задание 8. Использование модели

Наконец ты смог обучить и протестировать модель, теперь ее можно применять либо интерпретировать результаты.

1. Выведи коэффициенты логистической регрессии и посмотри на значимость каждого признака для предсказания.
Интерпретируй данный результат, напиши, что сильно влияет на предсказание, а что нет, попробуй описать, почему получились такие результаты.
2. Создай функцию `predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, BMI, diabetes_pedigree_function, age)`, которая получает на вход признаки, делает все необходимые преобразования и дает прогноз вероятности наличия диабета.
3. Придумай свой пример и запусти на нем эту функцию.

Рекомендации:
* Для понимания, как оценить важность признаков, изучи, что такое логистическая регрессия и что означают коэффициенты логистической регрессии.
* Для понимания оценки вероятности необходимо также изучить устройство логистической, особенно то, как она вычисляет предсказание.

### Бонусное задание 9. Подбор гиперпараметров с использованием Grid Search

Чтобы улучшить качество и производительность модели, воспользуйся Grid Search для поиска оптимальных гиперпараметров.

1. Определи сетку гиперпараметров для логистической регрессии, например, регуляризацию C (слабее или сильнее) и выбор метода регуляризации (например, L1, L2).
2. С помощью GridSearchCV проведи перебор параметров на обучающей выборке, выбери лучшие параметры, ориентируясь на метрику ROC-AUC.
3. Переобучи модель с оптимальными параметрами и оцени ее производительность на тестовой выборке.
4. Сделай выводы о качестве работы новой модели и об эффективности метода Grid Search.

Рекомендация: после выполнения Grid Search выведи лучшие параметры и сравни метрики с базовой моделью. Проанализируй, насколько улучшилась производительность модели.

💡 [Нажми сюда](http://opros.so/jSVV1), **чтобы поделиться с нами обратной связью на этот проект**. Это анонимно и поможет команде Продукта сделать твоё обучение лучше.
