from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def logout_view(request):
    """log the user out """
    logout(request)
    return HttpResponseRedirect(reverse('workvisits:home'))


def register(request):
    """Register the user"""
    if request.method != 'POST':
        # Display blank User registration form
        print('register--------- not post')
        form = UserCreationForm()
    else:
        # process completed form
        print('register---------post')
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('workvisits:home'))
    context = {'form': form}
    return render(request, 'users/register.html', context)