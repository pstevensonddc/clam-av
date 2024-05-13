# views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    return render(request, 'home.html')



@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})