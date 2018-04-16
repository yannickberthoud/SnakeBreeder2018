from django.urls import path

from snake.views import IndexView, DetailView, OldSnakeView, SaleSnakeView, SearchSnakeView, NewBornView

app_name = 'snake'
urlpatterns = [
    path('a-vendre', SaleSnakeView.as_view(), name = 'sale'),
    path('recherches', SearchSnakeView.as_view(), name = 'search'),
    path('anciens-serpents', OldSnakeView.as_view(), name = 'old'),
    path('nouvelles-naissances', NewBornView.as_view(), name = 'newborn'),
    path('<str:family_slug>/<str:slug>', DetailView.as_view(), name = 'details'),
    path('<str:family_slug>', IndexView.as_view(), name = 'list'),
]