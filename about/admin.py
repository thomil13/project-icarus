from django.contrib import admin
from .models import AboutAuthor, AboutProject
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AboutAuthor)
class AboutAuthorAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(AboutProject)
class AboutProjectAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)