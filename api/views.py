from django.shortcuts import render
from tablib import Dataset
from api.models import Player, Team, crimeCategory, Details
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

class DetailsDetailView(DetailView):
    context_object_name = 'details'
    queryset = Details.objects.all()

def arrest_info(request, id=id):
    arrest_info = Details.objects.all()
    id = Details.objects.get(id)
    return render(request, 'arrestdetails/<int:id>', { 'arrest_info': arrest_info, 'id':id })

def details(request):
    search_term= ""
    if request.GET:
        search_term = request.GET['searchparams']
        results = Details.objects.filter(name__icontains=search_term)
        arrest_info = Details.objects.all()
        return render(request, 'arrestdetails.html', {'arrest_info': arrest_info, 'results': results, 'search_term': search_term})
    return render(request, 'arrestdetails.html',{})

def searchteams(request):
    search_term= ""
    if request.GET:
        search_term = request.GET['searchparams']
        team_search_results = Team.objects.filter(team_preffered_name__icontains=search_term)
        return render(request, 'teamsearch.html', {'team_search_results': team_search_results, 'search_term': search_term})
    return render(request, 'teamsearch.html',{})

def searchplayers(request):
    search_term= ""
    if request.GET:
        search_term = request.GET['searchparams']
        results = Player.objects.filter(Name__icontains=search_term)
        return render(request, 'playersearch.html', {'results': results, 'search_term': search_term})
    return render(request, 'playersearch.html',{})

def index(request):
    return render(request, 'index.html')

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['Player.json']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        crimecategory_resource = CrimeCategoryResource()
        dataset = Dataset()
        new_crime = request.FILES['crime.csv']

        imported_data = dataset.load(new_crime.read())
        result = crimecategory_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            crimecategory_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'crimecategory_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        team_resource = TeamResource()
        dataset = Dataset()
        team_crime = request.FILES['team.csv']

        imported_data = dataset.load(team_crime.read())
        result = team_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            team_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'team_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        details_resource = DetailsResource()
        dataset = Dataset()
        new_details = request.FILES['Details.csv']

        imported_data = dataset.load(new_details.read())
        result = details_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            details_resource.import_data(dataset, dry_run=False)  # Actually import now
