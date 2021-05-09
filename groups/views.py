from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # We just want the user edit name and description in the Group model
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
