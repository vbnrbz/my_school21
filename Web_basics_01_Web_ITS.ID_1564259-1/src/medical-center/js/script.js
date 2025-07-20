document.addEventListener('DOMContentLoaded', () => {
    // Подсветка активного пункта меню
    const currentPage = location.pathname.split("/").pop();
    document.querySelectorAll("nav ul li a").forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });

    // Всплывающая информация о врачах
    const doctorCards = document.querySelectorAll('.doctor-card');
    doctorCards.forEach(card => {
        card.addEventListener('click', () => {
            const info = card.querySelector('.doctor-info');
            info.style.display = info.style.display === 'block' ? 'none' : 'block';
        });
    });
});

const doctors = {
    ivanov: {
        name: "Д-р Иванов",
        specialty: "Кардиолог",
        info: "15 лет стажа, специализация — сердечно-сосудистая система. Выпускник МГМУ им. Сеченова."
    },
    petrova: {
        name: "Д-р Петрова",
        specialty: "Невролог",
        info: "Эксперт по расстройствам нервной системы, кандидат медицинских наук."
    },
    sidorov: {
        name: "Д-р Сидоров",
        specialty: "Хирург",
        info: "Проводит операции любой сложности, член Европейской ассоциации хирургов."
    }
};

const modal = document.getElementById("modal");
const modalName = document.getElementById("modal-name");
const modalSpecialty = document.getElementById("modal-specialty");
const modalInfo = document.getElementById("modal-info");
const closeBtn = document.querySelector(".close");

document.querySelectorAll(".doctor-card").forEach(card => {
    card.addEventListener("click", () => {
        const id = card.dataset.doctor;
        const doc = doctors[id];
        if (doc) {
            modalName.textContent = doc.name;
            modalSpecialty.textContent = doc.specialty;
            modalInfo.textContent = doc.info;
            modal.style.display = "block";
        }
    });
});

closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});
