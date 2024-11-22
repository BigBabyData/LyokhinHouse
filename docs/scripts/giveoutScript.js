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

// ИЗМЕНЕНИЕ ПОЛЕЙ И ИХ ОБРАБОТКА

document.addEventListener('DOMContentLoaded', function() {
    toggleAdditionalFields(); 
});

function toggleAdditionalFields() {
    const selectElement = document.getElementById('cat-breed');
    const additionalFields = document.getElementById('additional-fields');
    const sourceInput = document.getElementById('source');

    if (selectElement.value === 'Домашний') {
        additionalFields.style.display = 'block';
        sourceInput.placeholder = 'Причина сдачи'; 
        setRequired(true); 
    } else {
        additionalFields.style.display = 'none';
        sourceInput.placeholder = 'Где нашли'; 
        setRequired(false); 
    }
}

function setRequired(isRequired) {
    document.getElementById('breed').required = isRequired;
    document.getElementById('gender').required = isRequired;
    document.getElementById('name').required = isRequired;
}

// ФОРМА

document.getElementById('giveoutForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const formData = {
        fio: document.getElementById('fio').value,
        phone: document.getElementById('phone').value,
        cat_breed: document.getElementById('cat-breed').value,
        source: document.getElementById('source').value,
        breed: document.getElementById('breed').value || null,
        gender: document.getElementById('gender').value || null,
        name: document.getElementById('name').value || null,
    };

    // ОТПРАВКА ДАННЫХ НА СЕРВЕР

    fetch('/submit-application', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успех:', data);
        document.getElementById('giveoutForm').reset(); // Очистка формы
        alert('Заявка успешно отправлена!'); 
    })
    .catch((error) => {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при отправке заявки.');
    });
});