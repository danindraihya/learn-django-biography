from django.views.generic import ListView, TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'