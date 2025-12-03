from django.contrib import admin
from .models import ImagePost, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


@admin.register(ImagePost)
class ImagePostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ('title',)
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


admin.site.register(Comment)
