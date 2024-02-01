from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from upload_files.models import File
from upload_files.serializers import FileSerializer
from upload_files.tasks import upload_file
from rest_framework import generics


class FileUploadView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_instance = serializer.save()
        upload_file(file_instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
