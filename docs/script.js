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

// ПЕРЕКЛЮЧЕНИЕ ПОЛЯ НА СТРАНИЦЕ ОТДАТЬ В ПРИЮТ

function toggleAdditionalFields() {
    const selectElement = document.getElementById('cat-breed');
    const additionalFields = document.getElementById('additional-fields');
    const sourceInput = document.getElementById('source');

    if (selectElement.value === 'Уличный') {
        additionalFields.style.display = 'none';
        sourceInput.placeholder = 'Где нашли'; 
    } else {
        additionalFields.style.display = 'none';
        sourceInput.placeholder = 'Причина сдачи'; 
        additionalFields.style.display = 'block';
    }
}

// КАРТОЧКИ НА СТРАНИЦЕ "ВЗЯТЬ ИЗ ПРИЮТА"

const products = [
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
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
    { name: 'Лёха', age: '3 мес', description: 'Красив, молод и очень хочет домой.', img: 'img/image3.jpg' },
];

let currentPage = 0;
const itemsPerPage = 15; // Количество карточек на странице

function renderProducts() {
    const productList = document.querySelector('.takeFS-list');
    productList.innerHTML = ''; // Очистка текущих карточек

    const start = currentPage * itemsPerPage;
    const end = start + itemsPerPage;
    const pageProducts = products.slice(start, end);

    pageProducts.forEach(product => {
        const card = document.createElement('li');
        card.className = 'card';
        card.innerHTML = `
            <button class="card-button">
                <div class="card-content">
                    <img src="${product.img}" class="card-image" width="339" height="262">
                    <h3>${product.name}</h3>
                    <p class="age">${product.age}</p>
                    <p class="description">${product.description}</p>
                </div>
            </button>
        `;
        productList.appendChild(card);
    });

    updateButtons();
    // Прокрутка к секции "Забрать из приюта"
    document.querySelector('.takeFS-main').scrollIntoView({ behavior: 'smooth' });
}

// КНОПКИ НА СТРАНИЦЕ "ВЗЯТЬ ИЗ ПРИЮТА"

function updateButtons() {
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');

    prevButton.disabled = currentPage === 0; // Дизаблить кнопку, если на первой странице
    nextButton.disabled = (currentPage + 1) * itemsPerPage >= products.length; // Дизаблить кнопку, если на последней странице
}

document.getElementById('prev-button').addEventListener('click', () => {
    if (currentPage > 0) {
        currentPage--;
        renderProducts();
    }
});

document.getElementById('next-button').addEventListener('click', () => {
    if ((currentPage + 1) * itemsPerPage < products.length) {
        currentPage++;
        renderProducts();
    }
});

// ИНИЦИАЛИЗАЦИЯ

renderProducts();

