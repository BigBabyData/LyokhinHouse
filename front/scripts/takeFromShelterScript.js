// Удалите или закомментируйте локальный массив cats
// const cats = [ ... ваш старый массив ... ];

// Объявляем глобальную переменную cats
let cats = [];

// Функция получения котов с сервера
async function fetchCats() {
    try {
        const response = await fetch('https://lyokhinhouse-api.up.railway.app/get-cats-in-shelter', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой: ' + response.status);
        }

        const data = await response.json();
        console.log('Список котов:', data);

        // Сохраняем полученных котов в глобальную переменную cats
        cats = data.cats_in_shelter;

        // Отрисовываем котов
        renderCats();
    } catch (error) {
        console.error('Ошибка при получении списка котов:', error);
        alert('Произошла ошибка при получении данных.');
    }
}

// Подключение меню оставляем без изменений
document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.querySelector('.menu-but');
    const mobileMenu = document.querySelector('.mobile-menu');
    const closeButton = document.querySelector('.close-menu');

    menuButton.addEventListener('click', function() {
        mobileMenu.classList.add('open');
    });

    closeButton.addEventListener('click', function() {
        mobileMenu.classList.remove('open');
    });

    // Вызов fetchCats при загрузке страницы
    fetchCats();
});

// Инициализируем переменные для пагинации
let currentPage = 0;
const itemsPerPage = 15;

// Обновляем функцию renderCats, чтобы она использовала глобальный массив cats, полученный с сервера.
function renderCats() {
    const catsList = document.querySelector('.takeFS-list');
    catsList.innerHTML = ''; // Очистка текущих карточек

    const start = currentPage * itemsPerPage;
    const end = start + itemsPerPage;
    const pageCats = cats.slice(start, end);

    pageCats.forEach(cat => {
        const card = document.createElement('li');
        card.className = 'card';

        // В идеале, вам нужно будет добавить url страницы кота, image_url и т.д. из данных API
        card.addEventListener('click', () => {
            localStorage.setItem('selectedCat', JSON.stringify(cat));
            // Перейти на страницу кота, если в данных есть ссылка
            // Для примера используем cat1.html, но вы можете сделать маршрутизацию динамически
            window.location.href = 'cat-pages/cat1.html';
        });

        card.innerHTML = `
            <div class="card-content">
                <img src="${cat.image_url || 'img/image3.jpg'}" class="card-image" width="339" height="262">
                <h3>${cat.cat_name || 'Безымянный кот'}</h3>
                <p class="age">${cat.cat_age ? cat.cat_age + ' год(а/лет)' : 'Возраст не указан'}</p>
                <p class="description">${cat.description || 'Описание отсутствует'}</p>
            </div>
        `;

        catsList.appendChild(card);
    });

    updateButtons();
    document.querySelector('.takeFS-main').scrollIntoView({ behavior: 'smooth' });
}

function updateButtons() {
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');

    prevButton.disabled = currentPage === 0;
    nextButton.disabled = (currentPage + 1) * itemsPerPage >= cats.length;
}

document.getElementById('prev-button').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        renderCats();
    }
});

document.getElementById('next-button').addEventListener('click', () => {
    if ((currentPage + 1) * itemsPerPage < cats.length) {
        currentPage++;
        renderCats();
    }
});