from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . models import Case, Image

# Create your views here.
class CaseListView(ListView):
    context_object_name = 'cases'
    model = Case
    template_name = 'cases/CaseList.html'

class CaseCreateView(LoginRequiredMixin, CreateView):
    fields = ("img", "receiver_name", "description", "date")
    model = Case

class CaseUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("img", "receiver_name", "description", "date")
    model = Case

class CaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = reverse_lazy('cases:c_list')
