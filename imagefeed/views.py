from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ImagePost, Comment
from .forms import CommentForm, UserPostForm


# Create your views here.
class ImagePostListView(generic.ListView):
    queryset = ImagePost.objects.filter(status=1)
    template_name = "imagefeed/index.html"
    context_object_name = "post_list"
    paginate_by = 4


class UserImagePostListView(generic.ListView):
    """Display only posts by the logged-in user."""
    template_name = "imagefeed/my-posts.html"
    context_object_name = "post_list"
    paginate_by = 4

    def get_queryset(self):
        return ImagePost.objects.filter(uploaded_by=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super().dispatch(request, *args, **kwargs)


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = ImagePost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.image_post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "imagefeed/imagepost-detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
def delete_post(request, pk):
    """Delete a post if the user is the author."""
    post = get_object_or_404(ImagePost, pk=pk)

    if post.uploaded_by != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You cannot delete a post you did not create'
        )
        return redirect('imagepost_detail', slug=post.slug)

    post.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Post deleted successfully'
    )
    return redirect('home')


@login_required
def create_post(request):
    """Create a new post."""
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.uploaded_by = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post created successfully'
            )
            return redirect('imagepost_detail', slug=post.slug)
    else:
        form = UserPostForm()

    return render(
        request,
        'imagefeed/new-post.html',
        {
            'post_create_form': form,
        },
    )


@login_required
def edit_post(request, pk):
    """Edit a post if the user is the author."""
    post = get_object_or_404(ImagePost, pk=pk)

    if post.uploaded_by != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You cannot edit a post you did not create'
        )
        return redirect('imagepost_detail', slug=post.slug)

    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post updated successfully'
            )
            return redirect('imagepost_detail', slug=post.slug)
    else:
        form = UserPostForm(instance=post)

    return render(
        request,
        'imagefeed/edit-post.html',
        {
            'form': form,
            'post': post,
        },
    )


@login_required
def delete_comment(request, pk):
    """Delete a comment if the user is the author."""
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.image_post.slug

    if comment.author != request.user:
        messages.add_message(
            request, messages.ERROR,
            'You cannot delete a comment you did not create'
        )
        return redirect('imagepost_detail', slug=post_slug)

    comment.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Comment deleted successfully'
    )
    return redirect('imagepost_detail', slug=post_slug)


@login_required
def edit_comment(request, pk):
    """Edit a comment if the user is the author."""
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.image_post.slug

    if comment.author != request.user:
        return JsonResponse({
            'success': False,
            'message': 'You cannot edit a comment you did not create'
        })

    if request.method == 'POST':
        comment.body = request.POST.get('body')
        comment.save()
        return JsonResponse({
            'success': True,
            'message': 'Comment updated successfully'
        })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })
