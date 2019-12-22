from django.views import generic
from .models import Album,Song
from django.views.generic.edit import *
from django.urls import reverse,reverse_lazy


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongCreate(CreateView):
    model = Song
    fields = ['album','song_title','song_file']

    def get_context_data(self, **kwargs):
        context = super(SongCreate, self).get_context_data(**kwargs)
        context['album_id'] = self.kwargs['album_id']
        return context

    def get_success_url(self):
        return reverse('music:detail', kwargs={'pk': self.object.album_id})


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')
