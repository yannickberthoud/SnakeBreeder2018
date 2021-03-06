from django.urls import path

from snake.views import IndexView, DetailView, OldSnakeView, SaleSnakeView, NewBornView, SearchSnakeView, SaleSnakeDetailsView

app_name = 'snake'

urlpatterns = [
    path('a-vendre', SaleSnakeView.as_view(), name = 'sale'),
    path('a-vendre/<str:family_slug>/<str:slug>', SaleSnakeDetailsView.as_view(), name = 'sale_details'),
    path('recherches', SearchSnakeView.as_view(), name = 'search'),
    path('anciens-serpents', OldSnakeView.as_view(), name = 'old'),
    path('nouvelles-naissances', NewBornView.as_view(), name = 'newborn'),
    path('<str:family_slug>/<str:slug>', DetailView.as_view(), name = 'details'),
    path('<str:family_slug>', IndexView.as_view(), name = 'list'),
]