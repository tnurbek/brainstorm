from django.shortcuts import render
from django.contrib.auth.models import Group
from User.models import Player
from django.http import HttpResponse

# g1 = Group.objects.create(name='')
# users = Player.objects.all()

def create_group(request, pk):
    name = request.GET.get('name_group')
    g = Group.objects.create(name=name)
    owner = Player.objects.get(pk=pk)
    g.user_set.add(owner)

    return HttpResponse()


# Create your views here.
