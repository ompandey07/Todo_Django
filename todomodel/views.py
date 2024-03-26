from django.shortcuts import render , redirect
from todomodel.models import Userdata


def homepage (request):
    if request.method == 'GET':
        show_data = Userdata.objects.all()
        return render (request , 'index.html' , {'show_data' :show_data})
    else:
        user_input = request.POST.get('user_input')
        database = Userdata(user_input = user_input)
        database.save()

        return redirect ('homepage')

def edit (request , id):
    if request.method == 'POST':
        user = Userdata.objects.get(id=id)
        user.user_input = request.POST.get('user_input')
        user.save()
        return redirect ('homepage')
    else:
        value = Userdata.objects.get(id=id)
        return render (request , 'edit.html' , {'value' : value})


def delete (request , id):
    hero = Userdata.objects.get(id=id)
    hero.delete()
    return redirect('homepage')
