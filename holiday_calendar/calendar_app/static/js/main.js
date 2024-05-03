document.addEventListener("DOMContentLoaded", function () {
    const currentDate = new Date();
    let currentYear = currentDate.getFullYear();
    let currentMonth = currentDate.getMonth() + 1;
    const monthNames = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
    const calendarHeader = document.getElementById("currentMonthYear");

    function updateCalendar() {
        const firstDayOfMonth = new Date(currentYear, currentMonth - 1, 1);
        const lastDayOfMonth = new Date(currentYear, currentMonth, 0);

        calendarHeader.textContent = monthNames[currentMonth - 1] + " " + currentYear;
        const daysInMonth = lastDayOfMonth.getDate();
        const daysElement = document.querySelector(".calendar .days");
        daysElement.innerHTML = "";

        if (daysElement) { // Проверяем, существует ли элемент
            for (let i = 1; i <= daysInMonth; i++) {
                const day = document.createElement("div");
                day.classList.add("day");
                day.textContent = i;
                day.addEventListener("click", function () {
                    const selectedDay = i;
                    const currentMonthYear = document.getElementById("currentMonthYear").textContent;
                    const [currentMonth, currentYear] = currentMonthYear.split(" ");
                    const monthIndex = monthNames.indexOf(currentMonth) + 1;

                    window.location.href = `/day/${currentYear}/${monthIndex}/${selectedDay}/`;
                });
                daysElement.appendChild(day);
            }
        } else {
            console.error("Элемент .calendar .days не найден");
        }
    }


    document.getElementById("prevMonth").addEventListener("click", function () {
        if (currentMonth === 1) {
            currentMonth = 12;
            currentYear--;
        } else {
            currentMonth--;
        }
        updateCalendar();
    });

    document.getElementById("nextMonth").addEventListener("click", function () {
        if (currentMonth === 12) {
            currentMonth = 1;
            currentYear++;
        } else {
            currentMonth++;
        }
        updateCalendar();
    });

    updateCalendar();
});
