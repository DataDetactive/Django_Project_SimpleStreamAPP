from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
 

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})