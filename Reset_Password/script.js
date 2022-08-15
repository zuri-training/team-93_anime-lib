const togglePassword = document.querySelector("#togglePassword");
const togglePasswords = document.querySelector("#togglePasswords");
const password = document.getElementById("password");
const new_password = document.getElementById("new_password");

togglePassword.addEventListener("click", function () {
  // toggle the type attribute for password
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  // toggle the icon
  this.classList.toggle("bi-eye");
});

togglePasswords.addEventListener("click", function () {
  // toggle the type attribute for confirm password
  const type =
    new_password.getAttribute("type") === "password" ? "text" : "password";
  new_password.setAttribute("type", type);
  // toggle the icon
  this.classList.toggle("bi-eye");
});

// prevent form from clearing
const form = document.querySelector("form");
form.addEventListener("submit", function (e) {
  e.preventDefault();
});

// prevent inaccurate password fields
function toggle() {
  if (password.value === "" && new_password.value === "") {
    window.alert("Password fields are empty!");
  } else if (password.value.length < 6 && new_password.value.length < 6) {
    window.alert("Password should be at least 6 characters");
  } else if (password.value === new_password.value) {
    var blur = document.getElementById("blur");
    blur.classList.toggle("active");
    var popup = document.getElementById("popup");
    popup.classList.toggle("active");
  } else {
    window.alert("Passwords do not match!");
  }
}
