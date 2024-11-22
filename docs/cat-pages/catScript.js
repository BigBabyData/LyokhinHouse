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

// ГАЛЕРЕЯ

document.querySelectorAll('.thumbnail').forEach(thumbnail => {
    thumbnail.onclick = function(evt) {
        evt.preventDefault();
        const activeImage = document.getElementById('active-image');
        activeImage.src = this.src;
        console.log("click")
        document.querySelectorAll('.thumbnail').forEach(item => {
            item.classList.remove('active');
        });
        this.classList.add('active');
    };
});

// ОТПРАВКА ФОРМЫ

const uniqueId = localStorage.getItem('selectedCatId');

document.getElementById('adoptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const formData = {
        id: uniqueId,
        fio: document.getElementById('fio').value,
        phone: document.getElementById('phone').value,
        time: document.getElementById('time').value,
    };

    // ОТПРАВКА НА СЕРВЕР

    fetch('/submit', {
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
        console.log(id, fio, phone, time);
        console.error('Ошибка:', error);
        alert('Произошла ошибка при отправке заявки.');
    });
});
