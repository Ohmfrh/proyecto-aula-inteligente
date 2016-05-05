import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Usersys

from .forms import NameForm, EditForm


# Create your views here.
def index(request):
    users = Usersys.objects.all()
    edit_form = EditForm()

    # print request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            print request.POST['name']
            print request.POST['last_names']
            print request.POST['email']
            try:
                newUser = Usersys(name=request.POST['name'], last_names=request.POST['last_names'], email=request.POST['email'])
                newUser.save()
            except:
                print ":("

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/usuarios/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    context = {'users': users, 'form': form, 'edit_form': edit_form}
    return render(request, 'usuarios/index.html', context)


def usuario(request):
    id = request.GET['usrId']
    data = {}
    usr = Usersys.objects.get(pk=id)

    data['name'] = usr.name
    data['last_names'] = usr.last_names
    data['id'] = usr.pk
    data['email'] = usr.email

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')


def editar(request):
    users = Usersys.objects.all()
    form = NameForm()

    # print request
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        edit_form = EditForm(request.POST)

        # check whether it's valid:
        if edit_form.is_valid():
            name = request.POST['editName']
            last_names = request.POST['editLast_names']
            email = request.POST['editEmail']
            id = request.POST['editId']

            user = Usersys.objects.get(pk=id)

            user.name = name
            user.last_names = last_names
            user.email = email

            user.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/usuarios/')

    # if a GET (or any other method) we'll create a blank form
    else:
        edit_form = EditForm()

    context = {'users': users, 'form': form, 'edit_form': edit_form}
    return render(request, 'usuarios/index.html', context)