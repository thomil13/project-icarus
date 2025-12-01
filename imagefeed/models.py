from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending Approval"), (1, "Approved"))

# Create your models here.


class ImagePost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    alt_text = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f'{self.title} by {self.uploaded_by.username}'


class Comment(models.Model):
    image_post = models.ForeignKey(ImagePost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.author}'
