from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    ListView,
    DetailView,
)

from album.models import Album


class PublicAlbumListView(ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'album/index.html'
    queryset = Album.objects.filter(private=False)


class PrivateAlbumListView(ListView):
    model = Album
    context_object_name = 'albums'
    template_name = 'album/private.html'
    queryset = Album.objects.filter(private=True)


class PublicAlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'album/detail.html'
    queryset = Album.objects.filter(private=False)


class CreateAlbumView(View):

    @staticmethod
    def get(request):
        return render(request, 'album/new.html')
    
    @staticmethod
    def post(request):

        # get data
        try:
            name = request.POST['name']
            description = request.POST['description']
            private = request.POST.get('private', False)
            creator = request.POST.get('creator', 'anonymous')
        except Exception as e:
            return render(request, 'album/new.html', {'error': f'Field {str(e)} not provided.'})

        # create instance and save
        try:
            album = Album.objects.create(
                name=name,
                private=private,
                creator=creator,
                description=description,
            )
            messages.success(request, f'Successfully created "{name}" album.')
            return redirect(album)
        except Exception as e:
            return render(request, 'album/new.html', {'error': f'Error : {str(e)}'})
