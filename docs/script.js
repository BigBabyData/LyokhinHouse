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
function toggleAdditionalFields() {
    const selectElement = document.getElementById('cat-breed');
    const additionalFields = document.getElementById('additional-fields');
    const sourceInput = document.getElementById('source');

    if (selectElement.value === 'Домашний') {
        additionalFields.style.display = 'block';
        sourceInput.placeholder = 'Причина сдачи'; 
    } else {
        additionalFields.style.display = 'none';
        sourceInput.placeholder = 'Где нашли'; 
    }
}

