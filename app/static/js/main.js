document.querySelectorAll('.card a').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        const isExternal = this.getAttribute('target') === '_blank';

        if (isExternal) {
            return;
        }
        e.preventDefault();

        const main = document.querySelector('main');
        const sections = document.querySelectorAll('main section');
        const cardsContainer = document.querySelector('.card__container');

        if (main) main.classList.add('fade-out');
        sections.forEach(sec => sec.classList.add('fade-out'));
        if (cardsContainer) cardsContainer.classList.add('fade-out');

        setTimeout(() => {
            window.location.href = href;
        }, 800);
    });
});

