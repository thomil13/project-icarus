from . import views
from django.urls import path


urlpatterns = [
    path('', views.ImagePostListView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='imagepost_detail'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]
