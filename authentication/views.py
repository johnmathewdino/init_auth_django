from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from authentication.forms import UserRegistrationForm


# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()


    return render(request, 'authentication/register.html',{
        'form': form
    })