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

    const buttonsDelete = document.getElementsByClassName("delete-btn");
    const modalDelete = new bootstrap.Modal(document.getElementById("modalDelete"));
    const confirmDelete = document.getElementById("confirmDelete");



    /*
    FUnctions changed to try and fix del button 
    const modalDelete = new bootstrap.Modal(document.getElementById("modalDelete"));
    
    const buttonsDelete = this.getElementsByClassName("delete-btn");
    console.log("Delete buttons found:", buttonsDelete.length);
    const confirmDelete = document.getElementById("confirmDelete");
    */

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
    
/* DELETE COMMENT BEFORE TRY AT FIXING
    for (let button of buttonsDelete) {
        button.addEventListener("click", (event) =>
        {let commentId = event.target.getAttribute("comment_id");
            console.log("Delete Button Clicked, comment ID:", commentId);
            confirmDelete.setAttribute = 'href', 'delete_comment/${commentId}';
            modalDelete.show();
    });
    }*/

    
    for (let button of buttonsDelete) {
        button.addEventListener("click", (event) => {
            let commentId = event.target.getAttribute("comment_id");
            console.log("Delete Button Clicked, comment ID:", commentId);
            
            confirmDelete.setAttribute('data-comment-id', commentId);
            
            modalDelete.show();
        });
    }

    confirmDelete.addEventListener("click", function(event) {
        event.preventDefault();
        console.log("Confirm delete clicked");
        
        const commentId = this.getAttribute('data-comment-id');
        const url = `/delete_comment/${post_slug}/${commentId}/`;
        console.log("Delete URL:", url);

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Comment deleted successfully", data);
                const commentElement = document.querySelector(`.comment-item:has(button[comment_id="${commentId}"])`);
                if (commentElement) {
                    commentElement.remove();
                }
                modalDelete.hide();
            } else {
                console.error('Error deleting comment:', data.error);
                alert(data.error);
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
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
