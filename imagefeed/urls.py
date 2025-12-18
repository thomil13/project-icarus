from . import views
from django.urls import path


urlpatterns = [
    path('', views.ImagePostListView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='imagepost_detail'),
]
