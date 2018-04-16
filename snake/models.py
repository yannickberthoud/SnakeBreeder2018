from django.db import models
from django.template.defaultfilters import slugify

from reptiles.models import Reptile

class Family(models.Model):
    """ Snake Model family """
    name = models.CharField(max_length = 32, verbose_name = "Nom")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        return super(Family, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Famille'
        verbose_name_plural = 'Familles'

class Venom(models.Model):
    name = models.CharField(max_length = 32, verbose_name = "Nom")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Toxicologie'
        verbose_name_plural = 'Toxixcologies'

class Snake(Reptile):
    """ Snake model """
    DENTITIONS = (
        ('A', 'Aglyphe'),
        ('O', 'Opistoglyphe'),
        ('P', 'Proteroglyphe'),
        ('I', 'Opistodonte'),
        ('S', 'Solenoglyphe')
    )
    family = models.ForeignKey(Family, on_delete = models.CASCADE)
    venom = models.ManyToManyField(Venom, blank = True)
    dentition = models.CharField(max_length = 1, choices = DENTITIONS, default = 'A')    
    old = models.BooleanField(blank = True, verbose_name = 'Ancien serpent')
    newborn = models.BooleanField(blank = True, verbose_name = 'Nouvelles naissances')

    def __str__(self):
        return self.scientific_name
    
    class Meta:
        verbose_name = 'Serpent'
        verbose_name_plural = 'Serpents'

class SearchingSnake(models.Model):
    species_list = models.TextField(verbose_name = "Liste d'espèces")

    def __str__(self):
        return self.species_list


class Album(models.Model):
    snake = models.ForeignKey(Snake, on_delete = models.CASCADE, related_name = "snakesalbum", related_query_name = "snakealbum")
    picture = models.ImageField(upload_to = 'public/uploads/snakes/')

    def __str__(self):
        return self.picture.path