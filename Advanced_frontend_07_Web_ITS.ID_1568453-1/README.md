# Расширенный фронтенд

Аннотация: \
В этом проекте ты будешь использовать React, чтобы сделать фронтенд для уже готового бэкенда.

## Содержание

1. [Chapter I](#chapter-i) \
   1.1. [Рекомендации к проекту](#рекомендации-к-проекту)
2. [Chapter III](#chapter-ii) \
   2.1. [Задание 1](#задание-1-базовое-reactприложение) \
   2.2. [Задание 2](#задание-2-работа-с-кабинетами) \
   2.3. [Задание 3](#задание-3-регистрация-доктора) \
   2.4. [Задание 4](#задание-4-регистрация-пациента) \
   2.5. [Задание 5](#задание-5-список-всех-докторов-с-возможностью-редактирования) \
   2.6. [Задание 6](#задание-6-список-всех-пациентов-с-возможностью-редактирования) \
   2.7. [Задание 7](#задание-7-настройка-маршрутизации-и-подключение-навигационного-меню-и-страницы) \
   2.8. [Бонусное Задание 8](#бонусное-задание-8-поиск-uuid-пациента-по-фио-и-дате-рождения) \
   2.9. [Бонусное Задание 9](#бонусное-задание-9-создание-встречи-с-подгрузкой-данных) \
   2.10. [Бонусное Задание 10](#бонусное-задание-10-отмена-встречи) \
   2.11. [Бонусное Задание 11](#бонусное-задание-11-детальная-информация-о-враче-с-управлением-встречами)

## Введение 

«Все круто, но надо переделать» — любой, услышав бы эту фразу от заказчика, рвал бы на себе волосы. Однако ты, уже наученный опытом общения с Вениамином и Клариссой, лишь спросил:

>— Что переделать?
>>**Стажер**

Буддийское спокойствие, которое в тебе воспитало общение с Главврачом, так просто не пробить...

>— Вот хотелось бы, чтобы встречи назначались как-то попроще, а то сейчас кажется, что нужны танцы с бубном. А также как-то покрасивее сделать все это, и еще вот тут бы...
>>**Вениамин**

Вениамин достал блокнот и перечислил список всего того, что еще вчера его не волновало. Будто всю ночь придумывал. Хотя тебе совершенно не казалась работа приложения «танцами с бубном», ты сделал глубокий вдох и ответил:

>— Хорошо, я переделаю. 
>>**Стажер**

«Спокойствие, только спокойствие, я в своем познании настолько преисполнился, я есть само олицетворение умиротворения...» — говорил ты сам себе, провожая приехавших клиентов. 

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

В прошлом проекте ты описал большой сервис с широкими возможностями для взаимодействия по REST API. Но для массового пользователя взаимодействие через API текстом и командами — немыслимое колдовство (еще и не особо удобное). В этом проекте ты соберешь фронтенд для приложения.

❗ _Ты можешь скопировать свое приложение из предыдущего проекта и продолжать работу над ним или взять уже готовое. Положи это приложение в директорию src._

Перед тем как приступить к разработке, создай логическую структуру приложения. Это поможет лучше понять архитектуру и связи между компонентами.

1. Создай схему приложения, где будут отображены:
    - бэкенд (серверная часть):
        * API endpoints,
        * база данных,
        * модели данных (Doctor, Patient, Appointment, Room);

    - фронтенд (клиентская часть):
        * компоненты React,
        * маршруты (Routes),
        * состояние приложения.

2. На схеме отобрази связи между:
    - бэкендом и базой данных;
    - фронтендом и бэкендом;
    - компонентами фронтенда между собой.

3. Для каждого компонента укажи:
    - его назначение;
    - с какими другими компонентами он взаимодействует;
    - какие данные обрабатывает.

Пример структуры:

```
[Бэкенд]
├── API
│   ├── /api/doctors
│   ├── /api/patients
│   ├── /api/appointments
│   └── /api/rooms
├── База данных
│   ├── Таблица doctors
│   ├── Таблица patients
│   ├── Таблица appointments
│   └── Таблица rooms

[Фронтенд]
├── Компоненты
│   ├── DoctorList
│   ├── PatientList
│   ├── AppointmentForm
│   └── RoomList
├── Маршруты
│   ├── /doctors
│   ├── /patients
│   ├── /appointments
│   └── /rooms
```

Эта схема поможет тебе:

- лучше понять архитектуру приложения,
- планировать разработку,
- видеть зависимости между компонентами.

### Задание 1. Базовое React-приложение

React-приложение — это отдельное приложение для фронтенда, которое будет отправлять запросы на бэкенд (если ты скопировал файлы из этого проекта, то это `hospital_project`) и отображать данные, которые приходят.

_Если еще не встречал слово CRUD, посмотри его значение._

В папке src создай новое приложение и подключи зависимости:

1. Создай React‑приложение с помощью Create React App.
2. Установи дополнительные зависимости:
   - axios для HTTP-запросов,
   - react-router-dom для маршрутизации,
   - bootstrap для оформления.
3. Подключи Bootstrap через CDN в index.html.
4. Подключи Bootstrap также и в index.js и отрендери приложение через него.

**Что такое Bootstrap?**

Bootstrap — это популярный CSS-фреймворк, который предоставляет готовые стили и компоненты для создания современного и отзывчивого пользовательского интерфейса. Он включает в себя:

- готовые классы для сетки (grid system),
- компоненты (кнопки, формы, навигационные панели и т. д.),
- утилиты для отступов, цветов, типографики,
- адаптивный дизайн «из коробки».

_Подсказка: фронтенд-баги хорошо ловить при помощи инструментов разработчика в браузерах. Например, можно смотреть, что отправляется на бэкенд, включая такие данные, как эндпоинт, тело запроса, тело ответа и многое другое._

### Задание 2. Работа с кабинетами

1. Отображение списка кабинетов: сделай страницу, которая получает с `API` список кабинетов (GET `/api/room`) и выводит их в виде списка с использованием `Bootstrap`‑стилей.
2. Создание кабинета: реализуй форму для создания нового кабинета, которая отправляет данные на `API` (`/api/room/create`) методом `POST`.
3. Редактирование и удаление кабинета: добавь возможность редактировать кабинет (`PATCH`) и удалять его (`DELETE`) прямо в списке или на отдельной странице, используя соответствующие `API`‑методы.
4. Для метода `DELETE` добавь подтверждение удаления (например, через `модальное окно`).


**PATCH-запросы**

PATCH-запросы используются для частичного обновления ресурса. В отличие от PUT, который заменяет весь ресурс, PATCH позволяет обновить только указанные поля. Это более эффективно, так как:

- уменьшает объем передаваемых данных,
- позволяет обновлять только необходимые поля,
- снижает риск конфликтов при параллельном редактировании.

Пример PATCH-запроса:

```javascript
axios.patch('/api/doctors/:id', {
    specialty: 'Новая специальность',
    is_available: true
});
```

### Задание 3. Регистрация доктора

1. Создание формы регистрации: сделай страницу регистрации доктора, где пользователь вводит `username`, `password`, `ФИО` и `специальность`.
2. Отправка данных: при отправке формы данные должны передаваться на `API` (`/api/register/doctor`) методом `POST`.
3. Валидация и уведомление: обеспечь валидацию введенных данных и отобрази сообщение об успешной регистрации или ошибке.

### Задание 4. Регистрация пациента

1. Создание формы регистрации пациента: реализуй страницу регистрации, где пользователь вводит `username`, `password`, `ФИО` и `дату рождения`.
2. Отправка данных: отправь данные на `API` (`/api/register/patient`) методом `POST`.
3. Автоматический расчет возраста: убедись, что на сервере возраст пациента вычисляется автоматически.
4. Обратная связь: выведи сообщение об успешной регистрации или об ошибке.

### Задание 5. Список всех докторов с возможностью редактирования

1. Вывод списка докторов: сделай страницу, где с `API` (`/api/doctors/all`) подгружается список всех врачей.
2. Отображение ключевой информации: для каждого врача покажи `UUID`, `ФИО`, `специальность` и `статус доступности`.
3. Inline‑редактирование: добавь кнопку «Редактировать», которая позволяет обновлять данные доктора (`PATCH`‑запрос) непосредственно в списке.
4. Переход к деталям: также добавь кнопку «Подробнее», ведущую на детальную страницу врача (`/doctor/:doctorId`).

### Задание 6. Список всех пациентов с возможностью редактирования

1. Вывод списка пациентов: создай страницу, где отображается список всех пациентов, полученных с `API` (`/api/patients/all`).
2. Отображение информации: для каждого пациента покажи `UUID`, `ФИО`, `дату рождения` и `возраст`.
3. Inline‑редактирование: добавь возможность редактировать данные пациента (`PATCH`‑запрос) прямо в списке.
4. Обратная связь: при обновлении выводи сообщение об успешном сохранении или ошибке.

### Задание 7. Настройка маршрутизации и подключение навигационного меню и страницы

Чтобы собрать все уже сделанное на одной страничке, добавь маршруты до них. Для этого в файле `src/App.js`:

1. Настрой маршруты с использованием библиотеки `react-router-dom`.
2. Подключи навигационное меню — импортируй компонент Navbar и размести его в верхней части страницы.
3. Определи маршруты:
    - Создай маршруты (`Routes`) для каждой из страниц приложения, которые были сделаны.
    - Убедись, что маршруты корректно работают — при переходе по `URL` отображаются нужные компоненты, а навигационное меню обеспечивает удобный переход между страницами.

**Что такое маршрутизация в React?**

Маршрутизация (routing) — это процесс определения того, какой компонент в зависимости от URL должен отображаться в адресной строке браузера. React Router — это стандартная библиотека для маршрутизации в React-приложениях.

Основные компоненты React Router:

- `BrowserRouter` — корневой компонент, который обеспечивает маршрутизацию;
- `Route` — определяет соответствие между URL и компонентом;
- `Link` — компонент для навигации между страницами.

Пример настройки маршрутов:

```javascript
import {BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage/>}/>
                <Route path="/doctors" element={<DoctorsList/>}/>
                <Route path="/patients" element={<PatientsList/>}/>
                <Route path="/appointments" element={<AppointmentsPage/>}/>
            </Routes>
        </BrowserRouter>
    );
}
```

Пример навигации:

```javascript
// Использование Link
<Link to="/doctors">Список врачей</Link>

// Программная навигация
const navigate = useNavigate();
navigate('/doctors');
```

### Бонусное задание 8. Поиск UUID пациента по ФИО и дате рождения

1. Создание формы поиска: сделай страницу, где пользователь вводит `ФИО пациента` и `дату рождения`.
2. Отправка запроса: отправляй `GET`‑запрос на `API` (`/api/patient-lookup`) с указанными параметрами.
3. Вывод результата: покажи `UUID` пациента или сообщение об ошибке, если пациент не найден.

### Бонусное задание 9. Создание встречи с подгрузкой данных

1. Форма создания встречи: реализуй страницу с формой для создания встречи.
2. Подгрузка выпадающих списков: используй `API`‑эндпоинты для получения списка врачей (`/api/doctors/all`), пациентов (`/api/patients/all`) и кабинетов (`/api/room`). В селектах отображай только `ФИО` (для `врача` и `пациента`) и название `кабинета`, а в значениях отправляй `UUID` или `room_id`.
3. Настройка даты встречи: добавь возможность установить дату встречи через кнопку (установить дату следующего дня после 9:00 утра, с небольшим смещением, например, 9:05).
4. Отправка данных: при отправке формы отправь данные на `API` (`/api/appointments/create`) методом `POST` и отобрази сообщение об успехе или ошибке.

### Бонусное задание 10. Отмена встречи

1. Создание формы отмены встречи: сделай страницу, где пользователь вводит `UUID` встречи.
2. Отправка запроса: отправляй `POST`‑запрос на `API` (`/api/appointments/cancel`) с указанным `appointment_id`.
3. Обратная связь: выведи сообщение об успешной отмене встречи или об ошибке, если встреча не найдена.

### Бонусное задание 11. Детальная информация о враче с управлением встречами

1. Создание детальной страницы врача: реализуй страницу, которая получает данные врача по `UUID` (`/api/doctors/:doctorId`) и выводит подробную информацию (`ФИО`, `специальность`, `доступность`).
2. Вывод списка встреч: на этой странице также подгрузи список встреч данного врача через API (`/api/doctors/:doctorId/appointments`).
3. Отмена встречи: для каждой встречи, если она не отменена, добавь кнопку «Отменить встречу», которая отправляет запрос на отмену встречи и обновляет список встреч в реальном времени.

Это был большой проект, но ты только посмотри на его результат — работающее с бэкендом react-приложение! Получаешь данные, красиво их показываешь, даешь пользователю с ними работать, редактировать, удалять — просто кайф. :)

---

Когда ты вечером отправил наработки Вениамину и Клариссе, они ожидаемо тебя похвалили. Однако ты давно уже не верил их восторгам — наверняка уже завтра они проснутся и придумают, что же надо переделать. В сущности, они были милыми людьми, но вот как клиенты... 

Впрочем, ты не жаловался: в Лаборатории ходили слухи о гораздо более безжалостных заказчиках, так что Кларисса с Вениамином на их фоне были просто душками. Сегодня тебе как раз удалось перекинуться парой слов с коллегами и выяснить, что до этого Вениамин и Кларисса вовсе не появлялись в Лаборатории — по всему казалось, что они выросли буквально из-под земли. Что только подтвердило твои подозрения. 

💡 [Нажми сюда](https://oprosso.ru/p/ad3bc98eb2a54c0baf4679fa722b54df), **чтобы поделиться с нами обратной связью на этот проект**. Это анонимно и поможет команде Продукта сделать твое обучение лучше.