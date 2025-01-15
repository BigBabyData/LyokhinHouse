// // МЕНЮ

// document.addEventListener('DOMContentLoaded', function() {
//     const menuButton = document.querySelector('.menu-but');
//     const mobileMenu = document.querySelector('.mobile-menu');
//     const closeButton = document.querySelector('.close-menu');

//     menuButton.addEventListener('click', function() {
//         mobileMenu.classList.add('open');
//     });

//     closeButton.addEventListener('click', function() {
//         mobileMenu.classList.remove('open');
//     });
// });

// --- МЕНЮ (у вас это уже есть, дублирую чтобы было видно всё вместе) ---
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
});

// --- ПОЛУЧАЕМ КОТОВ С СЕРВЕРА И ВЫВОДИМ НА ГЛАВНУЮ СТРАНИЦУ ---
async function fetchCatsForIndex() {
    try {
        // Делаем GET-запрос к нашему API
        const response = await fetch('https://lyokhinhouse-api.up.railway.app/get-cats-in-shelter', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            // Если сервер ответил с ошибкой
            throw new Error('Ошибка при получении котов, статус: ' + response.status);
        }

        // Парсим ответ
        const data = await response.json();
        const catsFromServer = data.cats_in_shelter;  // массив котов

        // Берём первые 10 котов
        const catsToShow = catsFromServer.slice(0, 12);

        // Отрисовываем их на странице
        renderCatsOnIndex(catsToShow);

    } catch (error) {
        console.error('Ошибка при получении списка котов:', error);
        alert('Произошла ошибка при получении данных с сервера.');
    }
}

// Функция, которая вставляет карточки котов в раздел &laquo;Выбрать питомца&raquo;
function renderCatsOnIndex(catsArray) {
    const cardsContainer = document.querySelector('.adopt .cards'); 
    cardsContainer.innerHTML = ''; // на всякий случай очищаем

    catsArray.forEach((cat) => {
        // Создаём элемент li
        const card = document.createElement('li');
        card.className = 'card';

        // Внутренний HTML карточки
        card.innerHTML = `
            <div class="card-content">
                <img 
                    src="${cat.image_url || 'img/image3.jpg'}" 
                    class="card-image" 
                    width="339" 
                    height="262"
                    alt="Кот из приюта">
                <h3>${cat.cat_name || 'Безымянный кот'}</h3>
                <p class="age">
                    ${cat.cat_age ? cat.cat_age + ' год(а/лет)' : 'Возраст не указан'}
                </p>
                <p class="description">
                    ${cat.description || 'Описание отсутствует'}
                </p>
            </div>
        `;

        // Добавляем обработчик клика, чтобы при нажатии:
        // 1. Сохранить данные кота в localStorage
        // 2. Перейти на страницу cat1.html, которая умеет эти данные считать
        card.addEventListener('click', () => {
            localStorage.setItem('selectedCat', JSON.stringify(cat));
            window.location.href = 'cat-pages/cat1.html';
        });

        // Добавляем карточку на страницу
        cardsContainer.appendChild(card);
    });
}

// Когда DOM загрузился, запустим подгрузку котов
document.addEventListener('DOMContentLoaded', function() {
    fetchCatsForIndex();
});