
if (window.innerWidth < window.innerHeight) {
    var swiper = new Swiper('.sp-swiper-container', {
        slidesPerView: 1,
        speed: 1000,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
} else {
    var swiper = new Swiper('.sp-swiper-container', {
        slidesPerView: 3,
        speed: 1000,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
}

function showSpagesMenu(e) {
    document.getElementById("spSideBar").classList.toggle("showSideBar");
    e.classList.toggle("whiteMenuBar");
}