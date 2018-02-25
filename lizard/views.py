from django.views import generic

from lizard.models import Lizard

class DetailView(generic.DetailView):
    model = Lizard
    template_name = 'lizard/details.html'
