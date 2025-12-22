// Handle comment delete and edit buttons
document.addEventListener('DOMContentLoaded', function() {
    console.log('comments.js loaded');
    
    const deleteButtons = document.querySelectorAll('.btn-delete');
    const editButtons = document.querySelectorAll('.btn-edit');
    const deleteModal = document.getElementById('deleteModal');
    const editModal = document.getElementById('editModal');
    const confirmDeleteLink = document.getElementById('deleteConfirm');
    const editCommentForm = document.getElementById('editCommentForm');
    const editCommentBody = document.getElementById('editCommentBody');
    const editConfirm = document.getElementById('editConfirm');
    
    console.log('Delete buttons found:', deleteButtons.length);
    console.log('Edit buttons found:', editButtons.length);
    console.log('Delete modal:', deleteModal);
    console.log('Edit modal:', editModal);
    
    let currentEditCommentId = null;
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const commentId = this.getAttribute('data-comment_id');
            console.log('Delete comment clicked:', commentId);
            
            if (deleteModal) {
                // Show the modal
                const modal = new bootstrap.Modal(deleteModal);
                modal.show();
                
                // Set up the confirm button to delete
                if (confirmDeleteLink) {
                    confirmDeleteLink.href = `/comment/${commentId}/delete/`;
                }
            }
        });
    });
    
    editButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const commentId = this.getAttribute('data-comment_id');
            console.log('Edit comment clicked:', commentId);
            
            if (editModal) {
                // Get the current comment text
                const commentElement = document.getElementById('comment' + commentId);
                const currentText = commentElement.textContent.trim();
                
                // Set the textarea with current text
                editCommentBody.value = currentText;
                currentEditCommentId = commentId;
                
                // Show the modal
                const modal = new bootstrap.Modal(editModal);
                modal.show();
            }
        });
    });
    
    // Handle edit confirmation
    if (editConfirm) {
        editConfirm.addEventListener('click', function(e) {
            e.preventDefault();
            
            if (currentEditCommentId && editCommentBody.value.trim()) {
                const formData = new FormData();
                formData.append('body', editCommentBody.value);
                
                fetch(`/comment/${currentEditCommentId}/edit/`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Update the comment text in the DOM
                        const commentElement = document.getElementById('comment' + currentEditCommentId);
                        commentElement.innerHTML = editCommentBody.value.replace(/\n/g, '<br>');
                        
                        // Close the modal
                        const modal = bootstrap.Modal.getInstance(editModal);
                        modal.hide();
                        
                        console.log('Comment updated successfully');
                    } else {
                        alert('Error: ' + data.message);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while updating the comment');
                });
            } else {
                alert('Please enter a comment');
            }
        });
    }
});

