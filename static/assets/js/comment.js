//Get Edit Buttons
//document.addEventListener('DOMContentLoaded', function() {
    

//const editBtns = document.getElementsByClassName("edit-btn");
//const commentInput = document.querySelector("#id_body");
//const commentFormElement = document.querySelector("#commentForm");
//const submitBtn = document.querySelector("#buttonSubmit");

//for (let btn of editBtns) {
//    btn.addEventListener("click", (event) => {
//        let commentId = event.target.getAttribute("comment_id");
//        let commentContent = document.getElementById(`comment${commentId}`).innerText;
//        commentInput.value = commentContent.trim();
//        submitBtn.innerText = "Update";
//        commentFormElement.setAttribute("action", `/${post_slug}/comment_edit/${commentId}/`);
//    });
//}
//});

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded");
    const editBtns = document.getElementsByClassName("edit-btn");
    console.log("Edit buttons found:", editBtns.length);

    const commentInput = document.querySelector("#id_body");
    const commentFormElement = document.querySelector("#commentForm");
    const submitBtn = document.querySelector("#buttonSubmit");
    const modalDelete = new bootstrap.Modal(document.getElementById("modalDelete"));
    
    const buttonsDelete = this.getElementsByClassName("delete-btn");
    console.log("Delete buttons found:", buttonsDelete.length);
    const confirmDelete = document.getElementById("confirmDelete");

    for (let btn of editBtns) {
        btn.addEventListener("click", (event) => {
            console.log("Edit button clicked");
            let commentId = event.target.getAttribute("comment_id");
            console.log("Comment ID:", commentId);
            
            let commentElement = document.getElementById(`comment${commentId}`);
            console.log("Comment element found:", commentElement !== null);
            
            if (!commentElement) {
                console.error(`Comment element not found for ID: comment${commentId}`);
                return;
            }
            
            let commentContent = commentElement.innerText;
            console.log("Comment content:", commentContent);
           
            commentInput.value = commentContent.trim();
            submitBtn.innerText = "Update";
            
            let newAction = `/${post_slug}/comment_edit/${commentId}/`;
            console.log("Setting form action to:", newAction);
            commentFormElement.setAttribute("action", newAction);
            
            console.log("Form action is now:", commentFormElement.getAttribute("action"));

            commentFormElement.scrollIntoView({ behavior: "smooth" });
        });
    }
    

    for (let button of buttonsDelete) {
        button.addEventListener("click", (event) =>
        {let commentId = event.target.getAttribute("comment_id");
            console.log("Delete Button Clicked, comment ID:", commentId);
            confirmDelete.setAttribute = 'href', 'delete_comment/${commentId}';
            modalDelete.show();
    });
    }
});

    /*document.addEventListener('DOMContentLoaded', function() {
        const editBtns = document.getElementsByClassName("edit-btn");
        const editCommentModal = new bootstrap.Modal(document.getElementById('editCommentModal'));
        const editCommentForm = document.getElementById('editCommentForm');
        const editCommentBody = document.getElementById('editCommentBody');
        const editCommentId = document.getElementById('editCommentId');
        const updateCommentBtn = document.getElementById('updateCommentBtn');
    
        for (let btn of editBtns) {
            btn.addEventListener("click", (event) => {
                let commentId = event.target.getAttribute("comment_id");
                let commentContent = document.getElementById(`comment${commentId}`).innerText;
                editCommentBody.value = commentContent.trim();
                editCommentId.value = commentId;
                editCommentModal.show();
            });
        }
    
        updateCommentBtn.addEventListener("click", () => {
            let commentId = editCommentId.value;
            let newAction = `/${post_slug}/comment_edit/${commentId}/`;
            editCommentForm.setAttribute("action", newAction);
            editCommentForm.submit();
            editCommentModal.hide();
        });
    });*/
