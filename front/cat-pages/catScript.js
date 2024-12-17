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

// // ГАЛЕРЕЯ

// document.addEventListener('DOMContentLoaded', () => {
//     const selectedCat = JSON.parse(localStorage.getItem('selectedCat'));

//     if (selectedCat) {
//         document.querySelector('.cat-name').textContent = selectedCat.name;
//         document.querySelector('.age').textContent = selectedCat.age;
//         document.querySelector('.cat-page-description').textContent = selectedCat.description;

//         // Устанавливаем активное изображение
//         const activeImage = document.getElementById('active-image');
//         activeImage.src = selectedCat.img; // Основное изображение

//         // Создание галереи
//         const thumbnailContainer = document.getElementById('thumbnail-container');
//         selectedCat.gallery.forEach((image, index) => {
//             const liElement = document.createElement('li');
//             const imgElement = document.createElement('img');
            
//             imgElement.src = image;
//             imgElement.alt = `Изображение ${index + 1}`;
//             imgElement.className = 'thumbnail';
//             if (index === 0) {
//                 imgElement.classList.add('active'); // Делаем первое изображение активным
//             }

//             // Обработчик клика для миниатюр
//             imgElement.addEventListener('click', () => {
//                 activeImage.src = image; // Обновляем активное изображение
//                 document.querySelectorAll('.thumbnail').forEach(item => {
//                     item.classList.remove('active');
//                 });
//                 imgElement.classList.add('active'); // Добавляем активный класс к текущему изображению
//             });

//             liElement.appendChild(imgElement);
//             thumbnailContainer.appendChild(liElement);
//         });

//         if (selectedCat.gallery.length > 0) {
//             activeImage.src = selectedCat.gallery[0]; // Устанавливаем первое изображение как активное
//         }
//     } else {
//         console.error('Кот не найден');
//     }

//     // Обработчик для кнопки "Назад"
//     document.querySelector('.back-button').addEventListener('click', () => {
//         window.history.back();
//     });
// });

// // ОТПРАВКА ФОРМЫ

// const uniqueId = localStorage.getItem('selectedCatId');
// let isSubmitting = false; // Флаг для отслеживания состояния отправки

// document.getElementById('adoptionForm').addEventListener('submit', function(event) {
//     event.preventDefault(); 

//     if (isSubmitting) return; // Проверка, выполняется ли уже запрос

//     isSubmitting = true; // Установка флага

//     const formData = {
//         id: uniqueId,
//         "full_name": document.getElementById('fio').value,
//         "phone_number": document.getElementById('phone').value,
//         "when_pick_up": document.getElementById('time').value,
//     };

//     // ОТПРАВКА НА СЕРВЕР

//     fetch('https://lyokhinhouse-api.up.railway.app/submit-take-cat', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(formData),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Успех:', data);
//         document.getElementById('adoptionForm').reset(); // Очистка формы
//         alert('Заявка успешно отправлена!'); 
//     })
//     .catch((error) => {
//         console.error('Ошибка:', error);
//         alert('Произошла ошибка при отправке заявки.');
//     })
//     .finally(() => {
//         isSubmitting = false; // Сброс флага после завершения
//     });
// });

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

// ГАЛЕРЕЯ И ОТОБРАЖЕНИЕ ДАННЫХ КОТА
document.addEventListener('DOMContentLoaded', () => {
    const selectedCat = JSON.parse(localStorage.getItem('selectedCat'));

    if (selectedCat) {
        // Отобразим данные кота
        document.querySelector('.cat-name').textContent = selectedCat.cat_name || 'Безымянный кот';
        document.querySelector('.age').textContent = selectedCat.cat_age ? `${selectedCat.cat_age} год(а/лет)` : 'Возраст не указан';
        document.querySelector('.cat-page-description').textContent = selectedCat.description || 'Описание отсутствует';

        // Устанавливаем активное изображение
        const activeImage = document.getElementById('active-image');
        activeImage.src = selectedCat.image_url || '../img/image3.jpg'; // Если нет url, можно подставить картинку-заглушку

        // Делаем заголовок "Забрать [Имя кота]"
        const adoptionHeader = document.querySelector('h2');
        if (adoptionHeader) {
            adoptionHeader.textContent = `Забрать ${"котика " + "«" + selectedCat.cat_name + "»" || 'котика'}`;
        }

        // Если галереи нет, закомментируем блок ниже или удалим:
        // const thumbnailContainer = document.getElementById('thumbnail-container');
        // if (selectedCat.gallery && selectedCat.gallery.length > 0) {
        //     selectedCat.gallery.forEach((image, index) => {
        //         const liElement = document.createElement('li');
        //         const imgElement = document.createElement('img');
        //         imgElement.src = image;
        //         imgElement.alt = `Изображение ${index + 1}`;
        //         imgElement.className = 'thumbnail';
        //         if (index === 0) {
        //             imgElement.classList.add('active');
        //             activeImage.src = image;
        //         }

        //         imgElement.addEventListener('click', () => {
        //             activeImage.src = image;
        //             document.querySelectorAll('.thumbnail').forEach(item => {
        //                 item.classList.remove('active');
        //             });
        //             imgElement.classList.add('active');
        //         });

        //         liElement.appendChild(imgElement);
        //         thumbnailContainer.appendChild(liElement);
        //     });
        // }

    } else {
        console.error('Кот не найден в localStorage');
    }
});

// ОТПРАВКА ФОРМЫ ЗАБРАТЬ КОТА
let isSubmitting = false;

document.getElementById('adoptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    if (isSubmitting) return;

    isSubmitting = true;

    const formData = {
        "full_name": document.getElementById('fio').value,
        "phone_number": document.getElementById('phone').value,
        "when_pick_up": document.getElementById('time').value,
    };

    fetch('https://lyokhinhouse-api.up.railway.app/submit-take-cat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успех:', data);
        document.getElementById('adoptionForm').reset();
        alert('Заявка успешно отправлена!');
    })
    .catch((error) => {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при отправке заявки.');
    })
    .finally(() => {
        isSubmitting = false;
    });
});