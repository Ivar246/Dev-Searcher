from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from  django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.
def loginUser(request):
    page = 'login'
    context={'page': page}
    
    
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist.')
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, 'logged in successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'username does not exist.')
        
    return render(request, 'users/login_register.html', context)
        
        
def logoutUser(request):
    logout(request)
    messages.success(request, 'Loggedout successfully.')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'user account was created.')
            
            login(request, user)
            return redirect('profile')
        else:
            
            messages.error(request, 'An error has occured dufing registration.')
            
    context={'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profile(request):
    profiles = Profile.objects.all()

    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="") 
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/user_profile.html', context)