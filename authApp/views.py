from django.shortcuts import render, redirect
from .forms import RegisterForm

# For logout
from django.contrib.auth import logout

# Create your views here.
def register(response):
    if(response.method == 'POST'):
        form = RegisterForm(response.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/daily-deals")
        else:
            return redirect("/register") 
    else:
       form = RegisterForm() 

    return render(response, "authApp/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/login")
