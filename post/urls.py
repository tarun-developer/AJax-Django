from django.conf.urls import url
from django.urls import include, path
from . import views
urlpatterns = [
        path('', views.index, name='index'),  # index view at /
        path('likepost/', views.likePost, name='likepost'),   # likepost view at /likepost
   ]