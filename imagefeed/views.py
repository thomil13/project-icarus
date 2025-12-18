from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import ImagePost
from .forms import CommentForm


# Create your views here.
class ImagePostListView(generic.ListView):
    queryset = ImagePost.objects.filter(status=1)
    template_name = "imagefeed/index.html"
    context_object_name = "post_list"
    paginate_by = 6


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
