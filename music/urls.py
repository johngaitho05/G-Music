from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('Album/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<int:pk>', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    path('song/add/<int:album_id>', views.SongCreate.as_view(), name='song-add'),
    path('song/<int:pk>/delete/', views.SongDelete.as_view(), name='song-delete'),
    path('play', views.play, name='play_song'),

]
