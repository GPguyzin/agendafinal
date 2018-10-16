from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path('post/cad', views.post_cad, name='post_cad'),
    path('post/ncad', views.post_ncad, name='post_ncad'),
    path('post/<int:pk>/detailcad', views.post_detailcad, name='post_detailcad'),
    path('post/<int:pk>/detailcad/editcad/', views.post_editcad, name='post_editcad'),
    path(r'^post/(?P<pk>\d+)/detail/remove/$', views.post_remove2, name='post_remove2'),


]