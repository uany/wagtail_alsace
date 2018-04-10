import 'foundation-sites/dist/css/foundation.min.css';

import './css/main.css';
import './css/header.css';
import './css/footer.css';

window.$(document).foundation();

/*
* Main navigation animation
* */
$(document).ready(() => {
    document.querySelector('.hamburger').addEventListener('click',() => {

    let isOpen = document.querySelector('.hamburger').classList
        .toggle('open');

    console.log(isOpen);

    if(isOpen){
        document.querySelector('#main-navigation').classList
            .toggle('open');

        document.querySelector('body').classList
            .toggle('no-scroll');

        window.scroll(0,0);

    }else{
         document.querySelector('#main-navigation').classList
            .toggle('closing');

        setTimeout(() => {
            document.querySelector('#main-navigation').classList
                .toggle('open');

            document.querySelector('#main-navigation').classList
                .toggle('closing');

            document.querySelector('body').classList
                .toggle('no-scroll');
        }, 400);
    }
});
});

