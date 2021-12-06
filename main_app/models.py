from django.db import models

from django.db.models import CharField, TextField, BooleanField, DateTimeField
from django.db.models.base import Model

# Create your models here.
class Videogame(models.Model):

    name = CharField(max_length=100)
    img = CharField(max_length=550)
    bio = TextField(max_length=500)
    retro_videogame = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Level(Model):
    title = CharField(max_length=150)
    element = CharField(max_length=150)
    boss = CharField(max_length=150)

    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE, related_name="levels") 

    def __str__(self):
        return self.title