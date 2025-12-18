// Handle comment delete and edit buttons
document.addEventListener('DOMContentLoaded', function() {
    console.log('comments.js loaded');
    
    const deleteButtons = document.querySelectorAll('.btn-delete');
    const editButtons = document.querySelectorAll('.btn-edit');
    const deleteModal = document.getElementById('deleteModal');
    const confirmDeleteLink = document.getElementById('deleteConfirm');
    
    console.log('Delete buttons found:', deleteButtons.length);
    console.log('Edit buttons found:', editButtons.length);
    console.log('Delete modal:', deleteModal);
    
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
                    confirmDeleteLink.href = `/imagefeed/comment/${commentId}/delete/`;
                }
            }
        });
    });
    
    editButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const commentId = this.getAttribute('data-comment_id');
            console.log('Edit comment clicked:', commentId);
            alert('Edit functionality coming soon');
            // window.location.href = `/imagefeed/comment/${commentId}/edit/`;
        });
    });
});
