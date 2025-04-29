const loginContainer = document.getElementById("loginContainer");
const loginButton = document.querySelector(".btn-login");

const signContainer = document.getElementById("signContainer");
const signButton = document.querySelector(".btn-signup");

const closeLoginBtn = document.getElementById("closeLoginBtn");
const closeSignBtn = document.getElementById("closeSignBtn");

// Switch between forms
const switchToSignup = document.getElementById("switchToSignup");
const switchToLogin = document.getElementById("switchToLogin");

// Ensure both forms are hidden initially
document.addEventListener("DOMContentLoaded", function() {
    loginContainer.style.display = "none";
    signContainer.style.display = "none";
});

// Open login form
loginButton.addEventListener("click", function(event) {
    event.stopPropagation();
    loginContainer.style.display = "flex";
    signContainer.style.display = "none"; // hide sign up
});

// Open signup form
signButton.addEventListener("click", function(event) {
    event.stopPropagation();
    signContainer.style.display = "flex";
    loginContainer.style.display = "none"; // hide login
});

// Switch to signup form
switchToSignup.addEventListener("click", function(event) {
    event.preventDefault();
    event.stopPropagation();
    loginContainer.style.display = "none";
    signContainer.style.display = "flex";
});

// Switch to login form
switchToLogin.addEventListener("click", function(event) {
    event.preventDefault();
    event.stopPropagation();
    signContainer.style.display = "none";
    loginContainer.style.display = "flex";
});

// Close login
closeLoginBtn.addEventListener("click", function(event) {
    event.stopPropagation();
    loginContainer.style.display = "none";
});

// Close signup
closeSignBtn.addEventListener("click", function(event) {
    event.stopPropagation();
    signContainer.style.display = "none";
});

// Clicking outside closes forms
window.addEventListener("click", function(event) {
    if (!loginContainer.contains(event.target) && event.target !== loginButton) {
        loginContainer.style.display = "none";
    }
    if (!signContainer.contains(event.target) && event.target !== signButton) {
        signContainer.style.display = "none";
    }
});
