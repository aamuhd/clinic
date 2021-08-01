
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from core.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from managing_staffs.models import Doctor, Nurse, Others
from . forms import DoctorRegistrationForm


def register_doctor(request):

    form = DoctorRegistrationForm()

    if request.method == 'POST':
        form = DoctorRegistrationForm(data=request.POST)
        if form.is_valid():
            group = Group.objects.get(name='doctor')

            user = form.save()
            user.groups.add(group)
            doctor = Doctor.objects.create(
                user = user,
                #email = instance.email,
                fullname = user.username
            
         
                )
            return redirect('/')

    context = {'form': form}

    return render(request, 'account/doctor_registration_form.html', context)




def register_nurse(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            group = Group.objects.get(name='nurse')

            user = form.save()
            user.groups.add(group)
            nurse = Nurse.objects.create(
                user = user,
                #email = instance.email,
                fullname = user.username
            
         
                )
            return redirect('/')

    context = {'form': form}

    return render(request, 'account/nurse_registration_form.html', context)



def login(request):
    
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is not correct')
            return redirect('/account/login/')

    else:
        return render(request, 'account/login.html', context)


def register(request):

    group = Group.objects.all()
    
    if request.method == 'POST':
        #first_name = request.POST['first_name']
        #last_name = request.POST['last_name']
        username = request.POST['username']
        #email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('/account/register/')

             
        
            #elif User.objects.filter(email=email).exists():
                #messages.info(request, 'Email exists')
                #return redirect(request, '/account/register/')
        
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                
                )

                user.save()

                return redirect('/')
        

    return render(request, 'account/register.html', {'group': group})



def logout(request):
    auth.logout(request)
    return redirect('/')

