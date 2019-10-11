from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Car


class CarView(TemplateView):
    template_name = 'django_drive_app/cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context
