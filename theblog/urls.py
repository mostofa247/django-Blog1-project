from django.urls import path
from . import views
from .views import HomeView,A_DetailView,AddPostView

urlpatterns = [
    #path('',views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('details/<int:pk>',A_DetailView.as_view(),name='details'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
]