from django.urls import path

from album.views import (
    CreateAlbumView,
    PublicAlbumListView,
    PublicAlbumDetailView,
)

app_name = 'album'

urlpatterns = [
    path('new/', CreateAlbumView.as_view(), name='new'),
    path('', PublicAlbumListView.as_view(), name='index'),
    path('detail/<int:pk>/', PublicAlbumDetailView.as_view(), name='detail'),
]
