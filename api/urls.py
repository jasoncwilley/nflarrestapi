from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
      path('', views.index, name='index'),
      path('playersearch/', views.searchplayers, name='searchplayers'),
      path('teamsearch/', views.searchteams, name='searchteams'),
      path('arrestdetails/', views.details, name='details')
]
