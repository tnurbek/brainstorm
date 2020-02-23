from django.shortcuts import render
from Group.models import Group
from Option.models import Option
from Task.models import Task
from User.models import Player

# g1 = Group.objects.create(name='')
# users = Player.objects.all()

def initial(request):
    options = Option.objects.all()
    return render(request, 'base.html', {'options':options})

def create_group(request):

    # if request.GET.get('group_name'):
    #     name = request.GET.get('group_name')
    # else:
    #     name = 'dwfwefewf'

    name = request.GET.get('group_name')
    # money = request.GET.get('money_field')
    # start = request.GET.get('start_time')
    start = '19:25:25'
    option_name = 'public'
    # option_name = request.GET.get('select')

    print(option_name)
    print(name)
    option = Option.objects.get(name=option_name)

    money = 0
    # start = '12:23:23'
    # option = Option.objects.get(pk=2)
    task_id = Task.objects.get(pk=1)
    g = Group.objects.create(name=name, money=money, start=start, task_id=task_id, option_id=option)
    owner = Player.objects.get(username=request.user.username)
    g.user_set.add(owner)
    if option.name == 'private':
        return render(request, 'group/password.html')
    elif option.name == 'public':
        return render(request, 'group/index.html')


# Create your views here.
