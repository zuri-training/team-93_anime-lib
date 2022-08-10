// first I get all the buttons in the ATTENTION SEEKERS using QUERYSELECTORALL
const micBtn = document.querySelectorAll("#micBtn");

// then I create a function which will handle the task each buttons should perform
function basicAnim() {
  // get
  let micImg = document.querySelector("#img1");

  // I used a FOR LOOP to loop through all the buttons 
  for (let i = 0; i < micBtn.length; i++) {
    micBtn[i].addEventListener("click", (e) => {
      
      // basically what I did here was if a button is clicked and the value of that button
        // matches the value in the IF STATEMENT an action should take place
      if (micBtn[i].value === "1") {

        // here I created a class in CSS then use JS to add the class also use
        // a setTimeout to reset the class to its initial state after 2sec
        micImg.className = "animated fadeInUp";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      } else if (micBtn[i].value === "2") {
        micImg.className = "animated fadeInDown";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      } else if (micBtn[i].value === "3") {
        micImg.className = "animated fadeInRight";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      } else if (micBtn[i].value === "4") {
        micImg.className = "animated fadeInLeft";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      } else if (micBtn[i].value === "5") {
        micImg.className = "animated bounce";
        setTimeout(() => {
          micImg.className = "arrowImg";
        }, 2000);

      } else if (micBtn[i].value === "6") {
        micImg.className = "animated blink";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      } else if (micBtn[i].value === "7") {
        micImg.className = "animated fadeOut";
        setTimeout(() => {
          micImg.className = "micImg";
        }, 2000);

      }
    });
  }
}
// I invoke the function here
basicAnim();
