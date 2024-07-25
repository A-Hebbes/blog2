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

    // Add event listener for the confirm delete button
confirmDelete.addEventListener("click", function(event) {
    event.preventDefault();
    
    const url = this.getAttribute('href');
    
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // You need to implement getCookie function
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log("Comment deleted successfully");
        // Remove the comment from the DOM
        const commentElement = document.getElementById(`comment${data.comment_id}`);
        if (commentElement) {
            commentElement.remove();
        }
        modalDelete.hide();
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error.message);
    });
});

// Function to get CSRF token
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
