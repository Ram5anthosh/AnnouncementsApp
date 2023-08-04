from django.shortcuts import render,redirect 
from .forms import MemberForm
from django.contrib import messages
from .models import Announcement
#from accounts.models import Account

# Create your views here.

def mkannouncements(request):
    if request.method=="POST":
        form = MemberForm(request.POST or None)
        
        #all_accounts = Account.objects.all
        #for item in all_accounts:
         #   if item.email == request.email:
          #      if item.passwd==request.passwd:
        if form.is_valid():
            form.save()
        else:
            messages.success(request,('There has been an error! Please retry...'))
            return redirect('mkannouncements')
        messages.success(request,('Your Announcement is created successfully!'))
        return redirect('home')
        #messages.success(request,('Please register first'))
        #return redirect('mkannouncements')
    else:
        return render(request, 'mkannouncements.html');

def display(request):
    all_announcements = Announcement.objects.all
    return render(request, 'display.html',{'all':all_announcements});

def view_announcements(request):
    all_announcements = Announcement.objects.all 
    return render(request, 'view_page.html',{'all' : all_announcements});
