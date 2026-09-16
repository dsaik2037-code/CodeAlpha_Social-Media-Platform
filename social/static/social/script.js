document.addEventListener("DOMContentLoaded", function () {

    // Like button confirmation
    const likeLinks = document.querySelectorAll(".like-button");

    likeLinks.forEach(function (button) {
        button.addEventListener("click", function () {
            button.style.transform = "scale(1.1)";

            setTimeout(function () {
                button.style.transform = "scale(1)";
            }, 150);
        });
    });

    // Comment form validation
    const commentForms = document.querySelectorAll(".comment-form");

    commentForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const input = form.querySelector(".comment-input");

            if (input.value.trim() === "") {
                event.preventDefault();
                alert("Please enter a comment.");
            }
        });
    });

    // Create post form validation
    const postForms = document.querySelectorAll(".post-form");

    postForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const content = form.querySelector("textarea");

            if (content && content.value.trim() === "") {
                event.preventDefault();
                alert("Please write something before creating a post.");
            }
        });
    });

});