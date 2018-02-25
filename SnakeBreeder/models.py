from django.db import models

class SlideShow(models.Model):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name
        
class Album(models.Model):
    picture = models.ImageField(upload_to = 'public/uploads/home/')
    album = models.ForeignKey(SlideShow, on_delete = models.CASCADE, related_name = "snakebreedersalbum", related_query_name = "snakebreederalbum")

    def __str__(self):
        return self.picture.path