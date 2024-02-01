from django.urls import path
from upload_files.views import FileUploadView, FileListView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('files/', FileListView.as_view(), name='file_list'),
]