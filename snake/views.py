from django.views import generic
from django.shortcuts import get_object_or_404

from snake.models import Family, Snake, SearchingSnake, SalingSnake

class IndexView(generic.ListView):
    template_name = 'snake/list.html'
    context_object_name = 'snakes'

    def get_queryset(self, **kwargs):
        """Return the last five published questions."""
        pk = get_object_or_404(Family, slug = self.kwargs['family_slug'])
        return Snake.objects.filter(family = pk, old = False).order_by('scientific_name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['family'] = Family.objects.get(slug = self.kwargs['family_slug'])
        return context

class NewBornView(generic.ListView):
    template_name = 'snake/list.html'
    context_object_name = 'snakes'

    def get_queryset(self, **kwargs):
        """Return the last five published questions."""
        return Snake.objects.filter(newborn = True).order_by('family', 'scientific_name')

class OldSnakeView(generic.ListView):
    template_name = 'snake/list.html'
    context_object_name = 'snakes'

    def get_queryset(self, **kwargs):
        """Return the last five published questions."""
        return Snake.objects.filter(old = True).order_by('family', 'scientific_name')

class SaleSnakeView(generic.ListView):
    template_name = 'snake/sale_list.html'
    context_object_name = 'snakes'

    def get_queryset(self, **kwargs):
        """Return the last five published questions."""
        return SalingSnake.objects.order_by('family', 'scientific_name')

class SaleSnakeDetailsView(generic.DetailView):
    model = SalingSnake
    template_name = 'snake/sale_details.html'
    context_object_name = 'snake'

class SearchSnakeView(generic.DetailView):
    #model = SearchingSnake
    template_name = 'snake/search_list.html'
    context_object_name = "object"

    def get_object(self):
        """Return the last five published questions."""
        return get_object_or_404(SearchingSnake, pk=1)

class DetailView(generic.DetailView):
    model = Snake
    template_name = 'snake/details.html'
