// МЕНЮ

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

// ЗАПРОС НА ПОЛУЧЕНИЕ КОТОВ ИЗ БД

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

        // Здесь вы можете обработать полученные данные и отобразить их на странице
        displayCats(data);
    } catch (error) {
        console.error('Ошибка при получении списка котов:', error);
        alert('Произошла ошибка при получении данных.');
    }
}

// КАРТОЧКИ НА СТРАНИЦЕ "ВЗЯТЬ ИЗ ПРИЮТА"

const cats = [
    { id: 0, name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg', url: 'cat-pages/cat1.html', gallery: ["../img/image2.jpg", "../img/image1mobile.jpg", "../img/image2.jpg"]},
    { id: 1, name: 'Вася', age: '5 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image1mobile.jpg', url: 'cat-pages/cat1.html', gallery: ["../img/image1mobile.jpg", "../img/image2.jpg", "../img/image2.jpg"] },
    { id: 2, name: 'Саша', age: '7 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg', url: 'cat-pages/cat1.html' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg', url: 'cat-pages/cat1.html'  },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg', url: 'cat-pages/cat1.html'  },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg', url: 'cat-pages/cat1.html'  },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
];

let currentPage = 0;
const itemsPerPage = 15; // Количество карточек на странице

function renderCats() {
    const catsList = document.querySelector('.takeFS-list');
    catsList.innerHTML = ''; // Очистка текущих карточек

    const start = currentPage * itemsPerPage;
    const end = start + itemsPerPage;
    const pageCats = cats.slice(start, end);

    pageCats.forEach(cat => {
        const card = document.createElement('li');
        card.className = 'card';

        card.addEventListener('click', () => {
            localStorage.setItem('selectedCat', JSON.stringify(cat)); // Сохранение всего объекта
            window.location.href = cat.url; // Перенаправление на уникальную страницу
     
        });

        card.innerHTML = `
            <div class="card-content">
                <img src="${cat.img}" class="card-image" width="339" height="262">
                <h3>${cat.name}</h3>
                <p class="age">${cat.age}</p>
                <p class="description">${cat.description}</p>
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

// ИНИЦИАЛИЗАЦИЯ
renderCats();


