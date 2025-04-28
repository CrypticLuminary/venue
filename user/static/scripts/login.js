const loginContainer = document.getElementById("loginContainer");
const loginButton = document.querySelector(".btn-login"); // Your external login button
const closeBtn = document.getElementById("closeBtn");

// Show login form
loginButton.addEventListener("click", function(event) {
    event.stopPropagation(); // Stop event from bubbling to window
    loginContainer.style.display = "flex"; // Show the form
});

// Hide login form when clicking on cross
closeBtn.addEventListener("click", function(event) {
    event.stopPropagation();
    loginContainer.style.display = "none"; // Hide the form
});

// Hide login form when clicking outside the form
window.addEventListener("click", function(event) {
    if (!loginContainer.contains(event.target) && event.target !== loginButton) {
        loginContainer.style.display = "none";
    }
});
