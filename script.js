document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const headerMenu = document.querySelector('.header-menu');

    hamburgerMenu.addEventListener('click', function () {
        headerMenu.classList.toggle('show'); 
    });
});


