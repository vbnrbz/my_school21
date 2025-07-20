doctors = [
    {
        "name": "Д-р Иванов",
        "specialty": "Кардиолог",
        "info": "Специалист по сердечно-сосудистой системе с 15-летним стажем."
    },
    {
        "name": "Д-р Петрова",
        "specialty": "Невролог",
        "info": "Эксперт в диагностике и лечении заболеваний нервной системы."
    },
    {
        "name": "Д-р Сидоров",
        "specialty": "Хирург",
        "info": "Проводит оперативные вмешательства любой сложности."
    }
]

# HTML шаблон страницы
html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Информация о врачах медицинского центра.">
    <title>Врачи - Медицинский центр</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header>
        <div class="header-container">
            <div class="logo">Здоровье</div>
            <nav role="navigation" aria-label="Основная навигация">
                <ul>
                    <li><a href="index.html">Главная</a></li>
                    <li><a href="about.html">О нас</a></li>
                    <li><a href="services.html">Услуги</a></li>
                    <li><a href="doctors.html" class="active">Врачи</a></li>
                    <li><a href="contacts.html">Контакты</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <div class="main-container">
{doctor_blocks}
        </div>
    </main>

    <footer>
        <p>&copy; 2025 Медицинский центр</p>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>
"""

# HTML блок одного врача
doctor_block_template = """            <section class="doctor-card">
                <h2>{name}</h2>
                <p><strong>{specialty}</strong></p>
                <div class="doctor-info" style="display: none;">
                    <p>{info}</p>
                </div>
            </section>"""

# Генерация HTML-контента для всех врачей
doctor_blocks = "\n".join([doctor_block_template.format(**doc) for doc in doctors])

# Запись в файл
with open("src/medical-center/doctors-script.html", "w", encoding="utf-8") as f:
    f.write(html_template.format(doctor_blocks=doctor_blocks))

print("Файл doctors-script.html успешно создан.")
