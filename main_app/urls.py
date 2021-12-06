# imports
# - the path to know what url to use
from django.urls import path
#  - views file
from . import views
# specific import
from .views import Home

# all urls.py files HAVE to have collections labeled urlpatterns
# this list will hold all urls inside of main_app
urlpatterns = [
  # path(url, function to run, name* optional)
  path('',views.Home.as_view(), name='home'),
  path('about/',views.About.as_view(), name='about'),
  path('videogames/',views.VideogameList.as_view(), name='videogame_list'),
  path('videogames/new',views.VideogameCreate.as_view(), name='videogame_create'),
  path('videogames/<int:pk>/',views.VideogameDetail.as_view(), name='videogame_detail'),
  path('videogames/<int:pk>/update',views.VideogameUpdate.as_view(), name='videogame_update'),
  path('videogames/<int:pk>/delete',views.VideogameDelete.as_view(), name='videogame_delete'),
  path('videogames/<int:pk>/level/new/',views.LevelCreate.as_view(), name='level_create'),
  path('videogames/<int:pk>/level/delete',views.LevelDelete.as_view(), name='level_delete'),
]
