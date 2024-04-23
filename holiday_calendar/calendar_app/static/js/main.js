document.addEventListener("DOMContentLoaded", function () {
    const currentDate = new Date();
    let currentYear = currentDate.getFullYear();
    let currentMonth = currentDate.getMonth() + 1; // Добавляем 1, так как месяцы в JavaScript нумеруются с 0
    const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
    const calendarHeader = document.getElementById("currentMonthYear");

    function updateCalendar() {
        const firstDayOfMonth = new Date(currentYear, currentMonth - 1, 1);
        const lastDayOfMonth = new Date(currentYear, currentMonth, 0);

        // Обновляем информацию в календаре
        calendarHeader.textContent = monthNames[currentMonth - 1] + " " + currentYear;
        const daysInMonth = lastDayOfMonth.getDate();
        const daysElement = document.querySelector(".calendar .days");
        daysElement.innerHTML = "";

        // Добавляем дни месяца
        for (let i = 1; i <= daysInMonth; i++) {
            const day = document.createElement("div");
            day.classList.add("day");
            day.textContent = i;
            daysElement.appendChild(day);
        }
    }

    document.getElementById("prevMonth").addEventListener("click", function () {
        if (currentMonth === 1) {
            currentMonth = 12;
        } else {
            currentMonth--;
        }
        updateCalendar();
    });

    document.getElementById("nextMonth").addEventListener("click", function () {
        if (currentMonth === 12) {
            currentMonth = 1;
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
            const monthIndex = monthNames.indexOf(currentMonth) + 1;

            // Перенаправляем пользователя на страницу с праздниками выбранного дня
            window.location.href = `/day/${currentYear}/${monthIndex}/${selectedDay}/`;
        }
    });

    // Инициализация календаря
    updateCalendar();
});
