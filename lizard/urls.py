from django.urls import path

from lizard.views import DetailView

app_name = 'lizard'
urlpatterns = [
    path('<str:slug>', DetailView.as_view(), name = 'details')
]