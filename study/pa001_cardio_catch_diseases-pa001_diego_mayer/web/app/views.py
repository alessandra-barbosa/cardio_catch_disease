from django.shortcuts import render, redirect
from .forms import PatientForm
from time import timezone

# Create your views here.

def form_post(request):

    if request.method == "POST":
        
        form = PatientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PatientForm()
    print(request)
    return render(request, 'app/form.html', {'form':form})

def prediction(request):
    render(request, 'app/prediction.html')