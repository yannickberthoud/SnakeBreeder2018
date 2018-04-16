from django.views import generic
from django.shortcuts import get_object_or_404, render

from snake.models import Family, Snake, SearchingSnake

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
    pass
#    template_name = 'snake/list.html'
#    context_object_name = 'snakes'
#    def get_queryset(self, **kwargs):
#        """Return the last five published questions."""
#        return Snake.objects.filter(business = 'A').order_by('family', 'scientific_name')

def SearchSnakeView(request):
    species_list = get_object_or_404(SearchingSnake, pk=1)
    return render(request, 'snake/search_list.html', {'species_list': species_list})

class DetailView(generic.DetailView):
    model = Snake
    template_name = 'snake/details.html'
