from django.shortcuts import render
from django.db.models import Q
from .models import Country

def country_list(request):
    # Get the search query from the GET request
    query = request.GET.get('q', '')
    
    # Filter countries based on the search query, case insensitive
    countries = Country.objects.filter(name__icontains=query) if query else Country.objects.all()
    
    # Render the template with the filtered countries
    return render(request, 'countries/country_list.html', {'countries': countries, 'query': query})
