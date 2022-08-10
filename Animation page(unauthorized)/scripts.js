// getting stuff

const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");

// for the basic animations

function change1(m){
    // remove the last class in img1
    // remove all classes
    img1.classList = "";
    // add m to class list
    img1.classList.add(m);
    // make it infinite
    // img1.classList.add('_repeat-infinite');
}
function change2(m){
    // remove the last class in img1
    // remove all classes
    img2.classList = "";
    // add m to class list
    img2.classList.add(m);
    // make it infinite
    // img2.classList.add('_repeat-infinite');
}


// did this here cos of webkit version and making the html messy THANKS 4 UNDEERSTANDING
// remove class again so you can click same animation btn twice and it works 
// STANDARD
img1.addEventListener('animationend', () => {
    img1.classList = "";
})
// CHROME, SAFARI, AND OPERA -i dont know why  they hve special one's but they are the guys that use webkit
img1.addEventListener('webkitAnimationEnd', () => {
    img1.classList = "";
})

// STANDARD
img2.addEventListener('animationend', () => {
    img2.classList = "";
})
// CHROME, SAFARI, AND OPERA -i dont know why  they hve special one's but they are the guys that use webkit
img2.addEventListener('webkitAnimationEnd', () => {
    img2.classList = "";
})