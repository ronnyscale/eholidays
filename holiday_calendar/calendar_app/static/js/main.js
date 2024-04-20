document.addEventListener("DOMContentLoaded", function () {
    const currentDate = new Date();
    let currentYear = currentDate.getFullYear();
    let currentMonth = currentDate.getMonth() + 1; // Добавляем 1, так как месяцы в JavaScript нумеруются с 0
    const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
    const calendarHeader = document.getElementById("currentMonthYear");

    function updateCalendar() {
    const firstDayOfMonth = new Date(currentYear, currentMonth - 1, 1); // Вычитаем 1, чтобы вернуться к нормальной нумерации месяцев
    const lastDayOfMonth = new Date(currentYear, currentMonth, 0); // Используем следующий месяц и 0 день, чтобы получить последний день текущего месяца
    const firstDayOfWeek = firstDayOfMonth.getDay();
    const daysInMonth = lastDayOfMonth.getDate();
    const daysElement = document.querySelector(".calendar .days");
    daysElement.innerHTML = "";

    calendarHeader.textContent = monthNames[currentMonth - 1] + " " + currentYear; // Вычитаем 1, чтобы вернуться к нормальной нумерации месяцев

    // Добавляем дни месяца
    for (let i = 1; i <= daysInMonth; i++) {
        const day = document.createElement("div");
        day.classList.add("day");
        day.textContent = i;
        daysElement.appendChild(day);
    }
}

    // Обработчики событий для кнопок переключения месяца
    document.getElementById("prevMonth").addEventListener("click", function () {
        if (currentMonth === 1) { // Если текущий месяц январь, переключаемся на декабрь предыдущего года
            currentMonth = 12;
            currentYear--;
        } else {
            currentMonth--;
        }
        updateCalendar();
    });

    document.getElementById("nextMonth").addEventListener("click", function () {
        if (currentMonth === 12) { // Если текущий месяц декабрь, переключаемся на январь следующего года
            currentMonth = 1;
            currentYear++;
        } else {
            currentMonth++;
        }
        updateCalendar();
    });

    // Добавляем обработчик события для клика на каждый день в календаре
    const daysElement = document.querySelector(".calendar .days");
    daysElement.addEventListener("click", function (event) {
        if (event.target.classList.contains("day")) {
            const selectedDay = event.target.textContent;
            const currentMonthYear = document.getElementById("currentMonthYear").textContent;
            const [currentMonth, currentYear] = currentMonthYear.split(" ");
            const monthIndex = monthNames.indexOf(currentMonth) + 1; // Получаем индекс месяца в массиве monthNames и добавляем 1, чтобы получить его числовое представление

            // Перенаправляем пользователя на страницу с праздниками выбранного дня
            window.location.href = `/day/${currentYear}/${monthIndex}/${selectedDay}/`;
        }
    });

    // Инициализация календаря
    updateCalendar();
});
