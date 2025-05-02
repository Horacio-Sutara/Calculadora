document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("click", (e) => {
            e.preventDefault(); // Prevenimos la navegación inmediata

            const href = card.getAttribute("href");
            const main = document.querySelector("main");

            if (main) {
                main.classList.add("fade-out");
            }

            setTimeout(() => {
                window.location.href = href;
            }, 600); // Igual duración que la animación
        });
    });
});
document.querySelectorAll('.volver-btn').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); // Evita la navegación inmediata

        const main = document.querySelector('main');
        main.classList.add('fade-out');

        setTimeout(() => {
            window.location.href = this.href;
        }, 500); // Tiempo para que la animación termine
    });
});
document.querySelectorAll('.volver-btn').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); // Evita la navegación inmediata

        // Agarramos todos los elementos que queremos animar
        const main = document.querySelector('main');
        const sections = document.querySelectorAll('main section');
        const cardsContainer = document.querySelector('.card__container');

        // Aplico la clase fade-out
        if (main) main.classList.add('fade-out');
        sections.forEach(sec => sec.classList.add('fade-out'));
        if (cardsContainer) cardsContainer.classList.add('fade-out');

        setTimeout(() => {
            window.location.href = this.href;
        }, 600); // Espera a que termine la animación
    });
});