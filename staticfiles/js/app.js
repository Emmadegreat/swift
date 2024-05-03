let see_more_btn = document.getElementById('btn');
let see_more_wrapper = document.getElementById('see-more-wrapper');
see_more_wrapper.style.display = 'none';

see_more_btn.addEventListener('click', () => {

    if (see_more_wrapper.style.display === 'none') {
        see_more_wrapper.style.display = 'block';
    } else {
        see_more_wrapper.style.display = 'none';
    }

    if (see_more_btn.textContent === 'See more') {
        see_more_btn.textContent = 'See less';
    } else {
        see_more_btn.textContent = 'See more';
    }

})