from django.urls import path
from .views import HomeView, AboutView, BaseView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('base/', BaseView.as_view(), name="base"),
]
