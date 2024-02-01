from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from upload_files.models import File


class FileModelTest(TestCase):
    def test_file_creation(self):
        file = b'file_content'
        uploaded_file = SimpleUploadedFile("testfile.txt", file, content_type="text/plain")
        file = File.objects.create(
            file=uploaded_file,
            processed=False
        )
        self.assertTrue(isinstance(file, File))
        self.assertFalse(file.processed)


class FileUploadTests(APITestCase):
    def test_upload_text_file(self):
        file_content = b'file_content'
        uploaded_file = SimpleUploadedFile("testfile.txt", file_content, content_type="text/plain")

        data = {'file': uploaded_file}

        url = reverse('file_upload')
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_upload_incorrect_format(self):
        file_content = b'file_content'
        uploaded_file = SimpleUploadedFile("testfile.json", file_content, content_type="text/plain")

        data = {'file': uploaded_file}

        url = reverse('file_upload')
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

