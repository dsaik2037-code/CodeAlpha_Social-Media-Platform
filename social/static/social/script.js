document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // LOGIN NOTIFICATION
    // =========================

    const loginForm = document.querySelector(".login-form");

    if (loginForm) {
        loginForm.addEventListener("submit", function () {
            alert("🔐 Logging in... Welcome to ConnectHub!");
        });
    }


    // =========================
    // LOGOUT NOTIFICATION
    // =========================

    const logoutButtons = document.querySelectorAll(".logout-btn");

    logoutButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {

            const confirmLogout = confirm(
                "🚪 Are you sure you want to logout?"
            );

            if (!confirmLogout) {
                event.preventDefault();
            }
        });
    });


    // =========================
    // LIKE BUTTON EFFECT
    // =========================

    const likeButtons = document.querySelectorAll(".like-button");

    likeButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            button.style.transform = "scale(1.15)";

            setTimeout(function () {
                button.style.transform = "scale(1)";
            }, 200);
        });
    });


    // =========================
    // COMMENT VALIDATION
    // =========================

    const commentForms = document.querySelectorAll(".comment-form");

    commentForms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const input = form.querySelector(".comment-input");

            if (input && input.value.trim() === "") {
                event.preventDefault();
                alert("💬 Please enter a comment.");
            }
        });

    });

});