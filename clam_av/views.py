# views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.base import ContentFile


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def scan(request):
    return Response({'message': 'We start to scan here!'})

@api_view(['GET'])
def test_spaces_connection(request):
    # Upload a file to DigitalOcean Spaces
    file_content = b'This is a test file content'
    file_name = 'test.txt'
    storage = S3Boto3Storage()
    storage.save(file_name, ContentFile(file_content))

    # Download the file from DigitalOcean Spaces
    file_content_downloaded = storage.open(file_name).read()

    # Compare uploaded and downloaded file content
    if file_content == file_content_downloaded:
        return HttpResponse('Connection to DigitalOcean Spaces is working!')
    else:
        return HttpResponse('Connection to DigitalOcean Spaces failed!')