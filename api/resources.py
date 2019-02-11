from import_export import resources
from .models import Player, crimeCategory, Team, Details

class PersonResource(resources.ModelResource):
    class Meta:
        model = Player

class CrimeCategoryResource(resources.ModelResource):
    class Meta:
        model = crimeCategory

class TeamResource(resources.ModelResource):
    class Meta:
        model = Team

class DetailsResource(resources.ModelResource):
    class Meta:
        model = Details
