from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
import os
from django.contrib.auth.decorators import login_required
from .models import UserProfile

from .forms import SignUpForm


def index(request):
    context = {}
    return render(request, 'easebrain/index.html', context)


class UserView(DetailView):
    template_name = 'easebrain/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('easebrain:profile')
    else:
        form = SignUpForm()
    return render(request, 'easebrain/signup.html', {'form': form})


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'profile': user_profile
    }
    return render(request, 'easebrain/profile.html', context)
