from django.shortcuts import render
from django.views.generic import ListView
from .models import Biography
from django.db.models import Q

class ListBiography(ListView):
    model = Biography
    template_name = 'biography/index.html'
    context_object_name = 'list_biography'

class ListSearch(ListView):
    model = Biography
    template_name = 'biography/search.html'
    context_object_name = 'list_biography'

    def get_queryset(self):
        query = self.request.GET.get('input_search')
        queryset = Biography.objects.filter(
            Q(name__contains=query)
        )
        return queryset