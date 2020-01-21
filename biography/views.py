from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import Biography
from django.db.models import Q
from .forms import BiographyForm
from django.urls import reverse_lazy

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

class DetailBiography(DetailView):
    model = Biography
    template_name = 'biography/detail.html'
    
class CreateBiography(CreateView):
    form_class = BiographyForm
    template_name = 'biography/create.html'

class ManageBiography(ListView):
    model = Biography
    template_name = 'biography/manage.html'
    context_object_name = 'list_biography'

class DeleteBiography(DeleteView):
    model = Biography
    template_name = 'biography/confirmation_delete.html'
    success_url = reverse_lazy('biography:manage')

class UpdateBiography(UpdateView):
    form_class = BiographyForm
    model = Biography
    template_name = 'biography/update.html'