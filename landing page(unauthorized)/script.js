 //Text
 const moveUp = document.querySelector(".moveUp");
 const moveDown = document.querySelector(".moveDown");
 const moveRight = document.querySelector(".moveRight");
 const moveLeft = document.querySelector(".moveLeft");
 const bounce = document.querySelector(".bounce");
 const blink = document.querySelector(".blink");
 const popOut = document.querySelector(".popOut");
 const shakeSide = document.querySelector(".shakeSide");



 //Buttons
 const btnMoveUp = document.querySelector(".btnMoveUp");
 const btnMoveDown = document.querySelector(".btnMoveDown");
 const btnMoveRight = document.querySelector(".btnMoveRight");
 const btnMoveLeft = document.querySelector(".btnMoveLeft");
 const btnBounce = document.querySelector("btnBounce");
 const btnBlink = document.querySelector(".btnBlink");
 const btnPopOut = document.querySelector(".btnPopOut");
 const btnShakeSide = document.querySelector(".btnShakeSide");



 //Functions
 btnMoveUp.addEventListener("click", () =>{
    moveUp.classList.toggle("moveUp");
 });
 btnMoveDown.addEventListener("click", () =>{
    moveDown.classList.toggle("moveDown");
 });

 btnMoveRight.addEventListener("click", () =>{
    moveRight.classList.toggle("moveRight")
 })