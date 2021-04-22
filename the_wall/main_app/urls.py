from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('thread/create', views.make_thread),
    path('comment/create', views.make_comment),
    path('comment/<int:comment_id>/delete', views.delete_comment),
    path('thread/<int:thread_id>/delete', views.delete_comment),
]