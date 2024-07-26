document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded");

    const editBtns = document.getElementsByClassName("edit-btn");
    const commentInput = document.querySelector("#id_body");
    const commentFormElement = document.querySelector("#commentForm");
    const submitBtn = document.querySelector("#buttonSubmit");
    const buttonsDelete = document.getElementsByClassName("delete-btn");
    const modalDelete = new bootstrap.Modal(document.getElementById("modalDelete"));
    const confirmDelete = document.getElementById("confirmDelete");

    console.log("Edit buttons found:", editBtns.length);
    console.log("Delete buttons found:", buttonsDelete.length);

    for (let btn of editBtns) {
        btn.addEventListener("click", (event) => {
            console.log("Edit button clicked");
            let commentId = event.target.getAttribute("comment_id");
            console.log("Comment ID:", commentId);
            
            let commentElement = document.getElementById(`comment${commentId}`);
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