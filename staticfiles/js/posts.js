// Handle delete post button
document.addEventListener('DOMContentLoaded', function() {
    console.log('posts.js loaded');
    
    const deleteButton = document.getElementById('postDelete');
    const editButton = document.getElementById('postEdit');
    const deletePostModal = document.getElementById('deletePostModal');
    const confirmDeleteBtn = document.getElementById('confirmDeletePost');
    
    console.log('Delete button:', deleteButton);
    console.log('Edit button:', editButton);
    console.log('Delete modal:', deletePostModal);
    
    if (deleteButton) {
        deleteButton.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Delete button clicked');
            const postId = this.getAttribute('data-post-id');
            console.log('Post ID:', postId);
            
            if (deletePostModal) {
                // Show the modal
                const modal = new bootstrap.Modal(deletePostModal);
                modal.show();
                
                // Set up the confirm button to delete
                if (confirmDeleteBtn) {
                    confirmDeleteBtn.href = `/imagefeed/post/${postId}/delete/`;
                }
            }
        });
    }
    
    if (editButton) {
        editButton.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Edit button clicked');
            const postId = this.getAttribute('data-post-id');
            console.log('Post ID:', postId);
            window.location.href = `/imagefeed/post/${postId}/edit/`;
        });
    }
});
