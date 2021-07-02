// card = document.querySelector('.card');
// card.classList.add('rotate-card')
// document.onkeydown = function(e){
//     if(e.keyCode == 38)
//     card = document.querySelector('.card');
//     card.classList.add('rotate_card');
//     card.classList.remove('card-hidden')
// }

let card_clicked = null;
let preventClick = false;
let matchFound = 0;
function onCardClicked(e){
    // card = document.querySelector('.card');

    // var card = document.getElementsByClassName('card');
    // card.classList.remove('card-hidden'); //nai hora bc sed feeling
    // setTimeout(() => {
    //     card.classList.add('card-hidden')
    // }, 1000);

    // console.log('cliiked', e.currentTarget);


    

    const target = e.currentTarget;
    // console.log(target.className);

    if(preventClick || target === card_clicked || target.className.includes('done')){
        return;
    }
    target.className = target.className.replace('card-hidden', '').trim();
    target.className += ' done';
    // console.log(target.getAttribute('data-color'));

    //first card
    if(!card_clicked){
        card_clicked = target;
    }
    
    //seond card  .. check and then eityher win win or close
    else if(card_clicked){
        if(card_clicked.getAttribute('data-color') !== target.getAttribute('data-color')){

            preventClick = true;

            setTimeout(() => {
                card_clicked.className = card_clicked.className.replace('done', '').trim() + ' card-hidden';
                target.className = target.className.replace('done', '').trim() + ' card-hidden';
                card_clicked=null;
                preventClick = false;

            }, 500);
        }
        else{
            matchFound++;
            card_clicked = null;
            if(matchFound===8){
                setTimeout(() => {
                    alert("you win");
                }, 500);
            }
        }
        
    }
}