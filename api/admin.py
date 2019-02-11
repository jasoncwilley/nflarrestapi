from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Player, crimeCategory, Team, Details

@admin.register(Player)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(crimeCategory)
class crimeCategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    pass

@admin.register(Details)
class DetailsAdmin(ImportExportModelAdmin):
    pass
