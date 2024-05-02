//TweenLite.defaultEase = Expo.easeOut;

let See_more_btn = document.getElementById('see-more-btn');
let See_more_cont = document.getElementById('see-more-cont');
See_more_cont.style.display = 'none';


function toggleSeeMore() {
    if (See_more_cont.style.display === 'none') {
        See_more_cont.style.display = 'grid';

        if (window.innerWidth <= 1024) {
            See_more_cont.style.gridTemplateColumns = 'repeat(1, 1fr)';

        }else if(window.innerWidth <= 600) {
            See_more_cont.style.gridTemplateColumns = 'repeat(1, 1fr)';

        } else {
            See_more_cont.style.gridTemplateColumns = 'repeat(3, 1fr)';
        }

    } else {
        See_more_cont.style.display = 'none';
    }

  See_more_btn.textContent = See_more_btn.textContent === 'See more' ? 'See less' : 'See more';
}

See_more_btn.addEventListener('click', toggleSeeMore);

// Add a resize event listener to update layout dynamically
window.addEventListener('resize', toggleSeeMore);


const contactCard = document.querySelectorAll(".contact-col");

contactCard.forEach(card => {
    const contactcard = card.querySelector(".contact-card");
    const icon = card.querySelector(".icon");

    contactcard.addEventListener('mouseover', () => {
        TweenLite.to(icon, 1, { rotation: 360 });
    })

    contactcard.addEventListener('mouseout', () => {
        TweenLite.to(icon, 1, { rotation: -360 });
    })
});

var date = new Date()

var time = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
document.getElementById('time').innerHTML = time;
document.getElementById("date").innerHTML = new Date().toDateString();


const col = document.querySelectorAll(".update-col");

col.forEach(card => {
    const cards = card.querySelector(".update-card");
    const body = card.querySelector(".update-body");
    const paragraph = card.querySelector(".pa");
    const read_more = card.querySelector(".read-more");
    //read_more.style.color = "#0d6efd";
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

        if (paragraph.style.color = "#fff") {
            paragraph.style.color = "#000";
        }

        if (read_more.style.color = "#198754") {
            read_more.style.color = "#198754";
            read_more.style.backgroundColor = "#f8f9fa";
        }
    })
});

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

/*

let btn = document.getElementById('btn');
let Notavailable = document.querySelectorAll('.not-available');
let addFieldBtn = document.getElementById('add-field');
let formFields = document.getElementById('form-fields');

Notavailable.forEach(element => {
    element.style.display = 'none';
    element.style.color='red';
});


btn.addEventListener("click", (e) => {
    e.preventDefault();

    Notavailable.forEach(element => {
        if (element.style.display === "none") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    });

})

addFieldBtn.addEventListener("click", (e) => {
    e.preventDefault();

    let newField = document.createElement('div');
    newField.classList.add('form-group');
    newField.innerHTML = `
        <label for="new-field">New Field:</label>
        <select name="new_field" id="new-field" class="form-control">
            <option value="option1">Option 1</option>
            <option value="option2">Option 2</option>
            <option value="option3">Option 3</option>
            <!-- Add more options as needed -->
        </select>
    `;
    formFields.appendChild(newField);
})


*/

/*function toggleSeeMore(width) {
    if (See_more_cont.style.display === 'none') {
        See_more_cont.style.display = 'grid';

        if (width <= 1024) {
            See_more_cont.style.gridTemplateColumns = width <= 600 ? 'repeat(1, 1fr)' : 'repeat(2, 1fr)';
        } else {
            See_more_cont.style.gridTemplateColumns = 'repeat(3, 1fr)';
        }
    } else {
        See_more_cont.style.display = 'none';
    }

    See_more_btn.textContent = See_more_btn.textContent === 'See more' ? 'See less' : 'See more';
}

function toggleSeeMoreOnClick() {
    toggleSeeMore(window.innerWidth);
}

function toggleSeeMoreOnResize() {
    toggleSeeMore(window.innerWidth);
}

See_more_btn.addEventListener('click', toggleSeeMoreOnClick);
window.addEventListener('resize', toggleSeeMoreOnResize);

// Call the function on page load to set initial layout
toggleSeeMore(window.innerWidth);*/




