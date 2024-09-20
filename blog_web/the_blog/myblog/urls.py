from django.urls import path
#from . import views
from .views import HomeView, ArticlesDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    #path('', views.home, name='home'),   
    path('', HomeView.as_view(), name= 'home'),
    path('articles/<int:pk>', ArticlesDetailView.as_view(), name= 'articles_detail'),
    path('add_post/', AddPostView.as_view(), name= 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name= 'delete_post'),
]
