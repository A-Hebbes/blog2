//Get Edit Buttons

const editBtns = document.getElementsByClassName("edit-btn");
const commentInput = document.querySelector("id_body");
const commentFormElement = document.querySelector("commentForm");
const submitBtn = document.querySelector("submitButton");

editBtns.forEach((btn) => {
    btn.addEventListener("click", (event) => {
        const commentId = event.target.getAttribute("comment_id");
        const commentContent = document.querySelector(`#comment${commentId}`).innerText;
        commentInput.value = commentContent;
        submitBtn.textContent = "Update";
        commentFormElement.setAttribute("action", `edit_comment/${commentId}`);
    });
});
