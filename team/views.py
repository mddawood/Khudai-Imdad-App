from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import MemberForm
from . models import Member
from django.views.generic import (ListView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Create your views here.
@login_required
def MemberCreateView(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('team:m_list')
    else:
        form = MemberForm()
    return render(request, 'team/AddMember.html', {'form' : form})

class MemeberListView(ListView):
    context_object_name = 'members'
    model = Member
    template_name = 'team/MemberList.html'

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'team/ProjectConfirmDelete.html'
    success_url = reverse_lazy('team:m_list')
