from django.db import models
from reptiles.models import Reptile

class Lizard(Reptile):
    """ Lizard model """

    class Meta:
        verbose_name = 'Lézard'
        verbose_name_plural = 'Lézards'

class Album(models.Model):
    lizard = models.ForeignKey(Lizard, on_delete = models.CASCADE, related_name = "lizardsalbum", related_query_name = "lizardalbum")
    picture = models.ImageField(upload_to = 'public/uploads/lizard/')

    def __str__(self):
        return self.picture.path