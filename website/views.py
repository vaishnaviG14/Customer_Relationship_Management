from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "Logged in successfully")
            else:
                messages.success(request, "Account is inactive") 
        else:
            messages.success(request, 'Enter correct credentials')
        
        return redirect('home')
    
    else:
        return render(request, 'home.html', {'records':records})



def record_details(request, req_id):
    if request.user.is_authenticated:
        requested_record = Record.objects.get(id=req_id)
        return render(request, 'record_details.html', {'requested_record':requested_record})
    else:
        messages.success(request, 'Please Login to access')
        return render(request, 'home.html', {})
    


def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid:
                add_record = form.save()
                messages.success(request, "Record added successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})

    else:
        messages.success(request, 'Please Login to access')
        return render(request, 'home.html', {})



def delete_record(request, req_id):
    if request.user.is_authenticated:
        rec = Record.objects.get(id=req_id)
        rec.delete()
        messages.success(request, "Record deleted successfully")
        return render(request, 'home.html', {})
    else:
        messages.success(request, 'Please Login to access')
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
