from django.shortcuts import render
from .models import AboutAuthor, AboutProject


def about(request):
    """Display the about page with author and project information."""
    aboutauthor = AboutAuthor.objects.first()
    aboutproject = AboutProject.objects.first()
    context = {
        'aboutauthor': aboutauthor,
        'aboutproject': aboutproject,
    }
    return render(request, 'about/about.html', context)
