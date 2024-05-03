const contactCard = document.querySelectorAll(".contact-col");

contactCard.forEach(card => {
    const contactcards = card.querySelector(".contact-card");
    const icon = card.querySelector(".icon");

    contactcards.addEventListener('mouseover', () => {
        TweenLite.to(icon, 1, { rotation: 360 });
    })

    contactcards.addEventListener('mouseout', () => {
        TweenLite.to(icon, 1, { rotation: -360 });
    })
});


//alert('hello world');

let date = new Date();

var time = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
document.getElementById('time').innerHTML = time;
document.getElementById("date").innerHTML = new Date().toDateString();



const col = document.querySelectorAll(".update-col");

col.forEach(card => {
    const cards = card.querySelector(".update-card");
    const body = card.querySelector(".update-body");
    const paragraph = card.querySelector(".pa");
    const read_more = card.querySelector(".read-more");
    //read_more.style.color = "red";
    cards.addEventListener("mouseenter", (e) => {
        e.preventDefault();

        if (body.style.backgroundColor = "#f8f9fa") {
            body.style.backgroundColor = "#198754";
        }

        if (paragraph.style.color = "#000") {
            paragraph.style.color = "#fff";
        }

        if (read_more.style.color = "#f8f9fa") {
            read_more.style.color = "#198754";
            read_more.style.backgroundColor = "#fff";
        }
    })

    cards.addEventListener("mouseleave", (e) => {
        e.preventDefault();
        if (body.style.backgroundColor = "#198754") {
            body.style.backgroundColor = "#f8f9fa";
        }

        if (paragraph.style.color ="#fff") {
            paragraph.style.color = "#000";
        }

        if (read_more.style.color = "#198754") {
            read_more.style.color = "#198754";
            read_more.style.backgroundColor = "#f8f9fa";
        }
    })
});



//back to top

let backtotop = document.querySelector('.back-to-top');

if (backtotop) {
    const ScrollBackToTop = () => {
        if (window.scrollY > 100) {
            backtotop.classList.add('active');
        } else {
            backtotop.classList.remove('active');
        }
    }
    window.addEventListener('load', ScrollBackToTop);
    window.addEventListener('scroll', ScrollBackToTop);
};