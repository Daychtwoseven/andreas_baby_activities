from django.contrib import messages
from django.shortcuts import render, redirect
from . decorators import login_required
from . models import Role, Person


@login_required
def index_page(request):
    try:
        context = {
            'data': None,
            'title': 'Home',
            'module_name': 'Home',
            'sidebar_active': 'home'
        }
        return render(request, 'frontend/index.html', context)
    except Exception as e:
        print(e)


@login_required
def persons_page(request, action=None, pk=None):
    try:
        context = {
            'data': None,
            'title': 'Persons',
            'module_name': 'Persons',
            'sidebar_active': 'persons'
        }
        if action is not None and pk is None:
            if action == 'add-role':
                name = request.POST.get('name')
                Role.objects.create(name=name)
                messages.success(request, "You have successfully added a Role.")
                return redirect('backend-persons-page')
            elif action == 'add-person':
                role_id = request.POST.get('role')
                name = request.POST.get('name')
                birthdate = request.POST.get('birthdate')
                Person.objects.create(role_id=role_id, name=name, birthdate=birthdate)
                messages.success(request, "You have successfully added a Person.")
                return redirect('backend-persons-page')

        context['data'] = Person.objects.all()
        return render(request, 'frontend/persons/index.html', context)
    except Exception as e:
        print(e)