from sys import path
from django.shortcuts import render
from django.views import generic
from .models import ImagePost

# Create your views here.


class ImagePostListView(generic.ListView):
    queryset = ImagePost.objects.all()
    template_name = 'index.html'
    context_object_name = 'imageposts'
    paginate_by = 6

    def get_queryset(self):
        return ImagePost.objects.all().order_by('-uploaded_at')
