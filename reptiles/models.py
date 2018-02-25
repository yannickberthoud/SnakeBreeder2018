from django.db import models
from django.template.defaultfilters import slugify

class Environment(models.Model):
    name = models.CharField(max_length = 32, verbose_name = "Nom")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Environnement'
        verbose_name_plural = 'Environnements'

class Repartition(models.Model):
    name = models.CharField(max_length = 64, verbose_name = "Nom")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Répartition'
        verbose_name_plural = 'Répartitions'

class Reptile(models.Model):
    """ Reptile abstract model """
    LIFES = (
        ('C', 'Crépusculaire'),
        ('D', 'Diurne'),
        ('N', 'Nocturne'),
    )
    REPRODUCTIONS = (
        ('O', 'Ovipare'),
        ('V', 'Vivipare'),
        ('I', 'Ovovipare'),
        ('P', 'Parthénogenèse')
    )
    MOEURS = (
        ('S', 'Semi-fouisseur'),
        ('F', 'Fouisseur'),
        ('T', 'Terrestre'),
        ('R', 'Semi-arboricole'),
        ('A', 'Arboricole')
    )
    scientific_name = models.CharField(max_length = 256, verbose_name = "Nom scientifique")
    slug = models.SlugField()
    description = models.TextField()
    sex = models.CharField(max_length = 11, help_text = 'format: x.y.z')
    moeurs = models.CharField(max_length = 1, verbose_name = "Moeurs", choices = MOEURS, default = 'A')
    repartition = models.ManyToManyField(Repartition)
    reproduction = models.CharField(max_length = 1, verbose_name = "Reproduction", choices = REPRODUCTIONS, default = 'O')
    life = models.CharField(max_length = 1, verbose_name = "Mode de vie", choices = LIFES, default = 'N')
    environment = models.ManyToManyField(Environment)

    def __str__(self):
        return self.scientific_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.scientific_name)
        return super(Reptile, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        verbose_name = 'Reptile'
        verbose_name_plural = 'Reptiles'
