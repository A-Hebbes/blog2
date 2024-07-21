//Get Edit Buttons
document.addEventListener('DOMContentLoaded', function() {
const editBtns = document.getElementsByClassName("edit-btn");
const commentInput = document.querySelector("#id_body");
const commentFormElement = document.querySelector("#commentForm");
const submitBtn = document.querySelector("#buttonSubmit");

for (let btn of editBtns) {
    btn.addEventListener("click", (event) => {
        let commentId = event.target.getAttribute("comment_id");
        let commentContent = event.target.closest('.comment').querySelector('.comment-content').innerText;
        commentInput.value = commentContent;
        submitBtn.innerText = "Update";
        commentFormElement.setAttribute("action", `comment_edit/${commentId}`);
    });
}
});
