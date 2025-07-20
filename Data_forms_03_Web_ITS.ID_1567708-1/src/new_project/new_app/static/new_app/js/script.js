
    // Подсветка активного пункта меню (на основе URL)
    const currentPage = window.location.pathname.split("/").pop();
    navLinks.forEach(link => {
      if (link.getAttribute('href') === currentPage) {
        link.classList.add('active');
      }
    });

    // Пример: Обработка кликов по изображениям врачей
    const doctorImages = document.querySelectorAll('img[alt*="Доктор"]');
    doctorImages.forEach(img => {
      img.addEventListener('click', function() {
        alert("Подробная информация о " + this.alt);
      });
    });

    // Обработка отправки контактной формы
    const contactForm = document.getElementById('contactForm');
    if(contactForm) {
      contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();
        let formMessage = document.getElementById('formMessage');

        if(name === "" || email === "" || message === "") {
          formMessage.innerText = "Все поля обязательны для заполнения.";
          formMessage.style.color = "red";
          return;
        }

        // Проверка email с помощью простого регулярного выражения
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailRegex.test(email)) {
          formMessage.innerText = "Введите корректный email.";
          formMessage.style.color = "red";
          return;
        }
      });
    } else {
  };
  