from django.shortcuts import render, get_object_or_404
from Group.models import Group
from Option.models import Option
from Task.models import Task
from User.models import Player
from .models import Password
# g1 = Group.objects.create(name='')
# users = Player.objects.all()

def initial(request):
    options = Option.objects.all()
    return render(request, 'group.html', {'options':options})

def create_group(request):

    a = request.POST.getlist('select', 'public')[0]
    name = request.POST.get('group_name')
    # else:
    #     a = 'public'
    #     name = 'nobody'

    # name = request.POST['group_name']
    # start = request.GET.get('start_time')
    start = '19:25:25'
    # option_name = 'public'
    # option_name = request.GET.get('value')

    option = Option.objects.get(name=a)

    money = 0

    task_id = Task.objects.get(pk=1)
    g = Group.objects.create(name=name, money=money, start=start, task_id=task_id, option_id=option)
    owner = Player.objects.get(username=request.user.username)
    g.user_set.add(owner)
    if option.name == 'private':
        return render(request, 'group/password.html', {'g_id':g.id})
    elif option.name == 'public':
        return render(request, 'group/index.html')

def validate_group(request, pk):
    password = request.POST.get('password')
    group = Group.objects.get(pk=pk)
    p = Password.objects.create(password=password, group_id=group)
    return render(request, 'group/index.html')



