from django.db.models import Q
from django.contrib import messages
from django.views.generic import View, ListView
from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404,
)

from album.models import Album
from uploader.models import Upload


class RecentUploadsView(ListView):
    model = Upload
    context_object_name = 'uploads'
    template_name = 'uploader/recent.html'
    queryset = Upload.objects.filter(album__private=False)[:10]


class CreateNewUploadView(View):

    @staticmethod
    def get(request):
        album_id = request.GET.get('album_id', None)
        if album_id is not None:
            albums = get_list_or_404(Album, pk=album_id, private=False)
        else:
            albums = Album.objects.filter(private=False)
        return render(request, 'uploader/upload.html', {
            'albums': albums
        })

    @staticmethod
    def post(request):

        album_id = request.GET.get('album_id', None)
        if album_id is not None:
            albums = get_list_or_404(Album, pk=album_id, private=False)
        else:
            albums = Album.objects.filter(private=False)

        # get data
        try:
            file = request.FILES['file']
            title = request.POST['title']
            album_id = request.POST['album_id']
            description = request.POST['description']
            creator = request.POST.get('creator', 'anonymous')

        except Exception as e:
            return render(request, 'uploader/upload.html', {
                'albums': albums,
                'error': f'Error : {str(e).title()} field not provided!'
            })

        try:

            album = get_object_or_404(Album, pk=album_id)

            upload = Upload.objects.create(
                file=file,
                title=title,
                album=album,
                creator=creator,
                description=description,
            )

            messages.success(request, f'Successfully added "{title}" to {album.name}.')
            return redirect(album)

        except Exception as e:
            return render(request, 'uploader/upload.html', {
                'albums': albums,
                'error': f'Error : {str(e).title()}'
            })


class UploadSearchView(View):

    @staticmethod
    def get(request):

        query = request.GET.get('query')

        if query is not None:

            queryset = Upload.objects.filter(
                Q(title__icontains=query) |
                Q(album__icontains=query) |
                Q(creator__icontains=query)
            ).distinct()

            return render(request, 'uploader/search.html', {
                'uploads': queryset    
            })

        else:

            return render(request, 'uploader/search.html')
