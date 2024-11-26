from django.urls import path
from .views import home, newsFeed

urlpatterns = [
    path('', home, name="home"),
    path('newsFeed', newsFeed, name="newsFeed")
]