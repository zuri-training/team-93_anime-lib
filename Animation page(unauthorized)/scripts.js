// getting stuff

const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");

// for the basic animations

function change1(m){
    // remove the last class in img1
    // remove all classes
    img1.classList = ""
    // add m to class list
    img1.classList.add(m);
    // make it infinite
    // img1.classList.add('_repeat-infinite');
}
function change2(m){
    // remove the last class in img1
    // remove all classes
    img2.classList = ""
    // add m to class list
    img2.classList.add(m);
    // make it infinite
    // img2.classList.add('_repeat-infinite');
}