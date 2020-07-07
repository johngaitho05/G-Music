from django.views import generic
from .models import Album,Song
from django.views.generic.edit import *
from django.urls import reverse,reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


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
    fields = ['song_file','song_title','artist']

    def get_context_data(self, **kwargs):
        context = super(SongCreate, self).get_context_data(**kwargs)
        context['album_id'] = self.kwargs['album_id']
        return context

    def get_success_url(self):
        return reverse('music:detail', kwargs={'pk': self.object.album_id})

    def form_valid(self, form):
        form.instance.album = get_object_or_404(Album, id=self.get_context_data()['album_id'])
        return super(SongCreate, self).form_valid(form)


class SongDelete(DeleteView):
    model = Song

    def get_success_url(self):
        return reverse('music:detail', kwargs={'pk': self.object.album_id})


def play(request):
    if request.method == 'POST':
        album_id = int(request.POST['album_id'])
        song_id = int(request.POST['song_id'])
        album = get_object_or_404(Album, id=album_id)
        song = get_object_or_404(Song, id=song_id)
        return render(request, 'music/detail.html',{'album':album,'to_play': song})

