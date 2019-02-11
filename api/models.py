from django.db import models

class Player(models.Model):
    id = models.IntegerField( primary_key=True)
    Name = models.CharField(max_length=30)
    Position = models.CharField(max_length=2)
    arrest_count = models.IntegerField()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']

class crimeCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=45)
    arrest_count = models.IntegerField()

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['arrest_count']

class Team(models.Model):
    id =  models.IntegerField(primary_key=True)
    team = models.CharField(max_length=3)
    team_preffered_name = models.CharField(max_length=25)
    team_name = models.CharField(max_length=25)
    team_city = models.CharField(max_length=25)
    team_conference = models.CharField(max_length=5)
    team_conference_division = models.CharField(max_length=15)
    team_logo_id =  models.IntegerField()
    arrest_count = models.IntegerField()

    def __str__(self):
        return self.team_preffered_name

    class Meta:
        ordering = ['arrest_count']

class Details(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(),
    team = models.CharField(max_length=3)
    team_preffered_name = models.CharField(max_length=25)
    team_name = models.CharField(max_length=25)
    team_city = models.CharField(max_length=25)
    team_conference = models.CharField(max_length=5)
    team_conference_division = models.CharField(max_length=15)
    team_hex_color = models.CharField(max_length=8)
    team_hex_alt_color	= models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=2)
    position_name = models.CharField(max_length=12)
    position_type = models.CharField(max_length=3)
    encounter = models.CharField(max_length=12)
    category = models.CharField(max_length=20)
    crime_category = models.CharField(max_length=20)
    crime_category_color = models.CharField(max_length=8)
    description = models.CharField(max_length=2000)
    outcome	 = models.CharField(max_length=2000)
    season = models.CharField(max_length=4)
    arrestseasonstate = models.CharField(max_length=20)
    year = models.CharField(max_length=12)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=10)
    day_of_week = models.CharField(max_length=10)
    day_of_week_int = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
