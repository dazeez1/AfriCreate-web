from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .forms import ProfileUpdateForm
from .models import UserProfile
from django.shortcuts import get_object_or_404


def mentorship(request):
    return render(request, 'mentorship.html')

def index(request):
    return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html')

def artists(request):
    return render(request, 'artists.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  
        else:
            print("Form is not valid")  
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm(request, initial={'username': ''})  

    return render(request, 'login.html', {'form': form})


@login_required
def index(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})


@login_required
def profile(request):
    user = request.user
    # Ensure the UserProfile instance exists
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("index")
    else:
        form = ProfileUpdateForm(instance=user_profile)

    context = {"form": form}
    return render(request, "index.html", context)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
