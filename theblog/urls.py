from django.urls import path
from . import views
from .views import HomeView,A_DetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    #path('',views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('details/<int:pk>',A_DetailView.as_view(),name='details'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('details/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('details/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]