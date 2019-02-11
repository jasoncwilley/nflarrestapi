from django.contrib import admin
from django.urls import path
from . import views
from api.views import DetailsDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
      path('', views.index, name='index'),
      path('playersearch/', views.searchplayers, name='searchplayers'),
      path('teamsearch/', views.searchteams, name='searchteams'),
      path('arrestdetails/', views.arrest_info, name='details'),
      path('details/<int:pk>', DetailsDetailView.as_view(), name='details_detail')
]
