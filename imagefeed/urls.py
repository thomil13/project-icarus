from . import views
from django.urls import path


urlpatterns = [
    path('', views.ImagePostListView.as_view(), name='imagepost_list'),
    path('<slug:slug>/', views.ImagePostListView.as_view(), name='imagepost_detail'),
]
