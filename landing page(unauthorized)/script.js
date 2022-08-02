 //Text
 const moveUp = document.querySelector("._moveUp");
 const moveDown = document.querySelector("._moveDown");
 const moveRight = document.querySelector("._moveRight");
 const moveLeft = document.querySelector("._moveLeft");
 const bounce = document.querySelector("._bounce");
 const blink = document.querySelector("._blink");
 const popOut = document.querySelector("._popOut");
 const shakeSide = document.querySelector("._shakeSide");



 //Buttons
 const btnMoveUp = document.querySelector(".btnMoveUp");
 const btnMoveDown = document.querySelector(".btnMoveDown");
 const btnMoveRight = document.querySelector(".btnMoveRight");
 const btnMoveLeft = document.querySelector(".btnMoveLeft");
 const btnBlink = document.querySelector(".btnBlink");
 const btnPopOut = document.querySelector(".btnPopOut");
 const btnShakeSide = document.querySelector(".btnShakeSide");



 //Functions
 btnMoveUp.addEventListener("click", () =>{
    moveUp.classList.toggle("_moveUp");
 });

 btnMoveDown.addEventListener("click", () =>{
    moveDown.classList.toggle("_moveDown");
 });

 btnMoveRight.addEventListener("click", () =>{
    moveRight.classList.toggle("_moveRight")
 })