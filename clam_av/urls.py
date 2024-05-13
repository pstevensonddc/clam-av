from django.urls import path, include
from .views import home
from .views import scan
from .views import test_spaces_connection

urlpatterns = [
    path('', home, name='home'),
    path('api/scan/', scan, name='scan'),
    path('api/test_upload/', test_spaces_connection, name='test_spaces_connection'),
]
