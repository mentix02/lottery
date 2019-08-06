from django.urls import path

from uploader.views import (
	RecentUploadsView,
	CreateNewUploadView,
)

app_name = 'uploader'

urlpatterns = [
	path('recent/', RecentUploadsView.as_view(), name='recent'),
	path('upload/', CreateNewUploadView.as_view(), name='upload'),
]
