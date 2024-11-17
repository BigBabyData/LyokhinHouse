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