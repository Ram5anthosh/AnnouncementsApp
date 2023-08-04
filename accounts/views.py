from django.shortcuts import redirect, render
from .forms import MemberForm 
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        #print(request.POST)
        form=MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            email = request.POST['email']
            passwd = request.POST['passwd']
            messages.success(request,('There has been an error! Please retry...'))
            #return redirect('register')
            return render(request,'register.html',{'email':email,
                                                   'passwd': passwd,})
        messages.success(request,('Your Account is created Successfully, wait for further access from the admin.'))
        return redirect('home')

    else:
        return render(request, 'register.html');


