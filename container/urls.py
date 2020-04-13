from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists/', views.rooms_list, name='lists_room'),
    path('create/', views.rooms_create, name='create_room'),
    path('upload/', views.upload_media, name='upload'),
    path('search/', views.rooms_search, name='search'),
    path('review/', views.create_review, name="create_review"),
    path('<int:id>', views.rooms_detail, name='detail_room'),
    path('<int:id>/edit/', views.rooms_update, name='update_room'),
    path('<int:id>/delete/', views.rooms_delete, name='delete_room'),
    path('<int:id>/update/', views.rooms_update, name='update'),

    path('<int:pk>/review/',
         views.new_review, name='give_review'),

]

app_name = 'rooms'
