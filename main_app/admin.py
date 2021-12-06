from django.contrib import admin

from .models import Videogame, Level
# Register your models here.

admin.site.register([Videogame, Level])