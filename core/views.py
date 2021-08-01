from django.views.generic import ListView, DetailView, View
from .helpers import Egg
from .models import MainPage, HomePageSlider, UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse, render, redirect
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist


# from blog.models import Post

# Create your views here.

class HomeView(View):
    template_name = "main/home.html"
    def get(self, *args, **kwargs):
        context = {}
        # context['posts'] = Post.objects.all().filter(publish=True).order_by('-pub_time')[:4]
        context['slider'] = HomePageSlider.objects.filter(active=True).first()
        return render(self.request, template_name='core/home.html', context=context)


class MainPageDetailView(DetailView):
    template_name = "core/pages.html" #.format(themeVersion() )
    model = MainPage
    query_pk_and_slug = True
    context_object_name = 'page'
    
    
    def get_context_data(self, *args, **kwargs):  
        try:  
            context = {}          
            context = super(MainPageDetailView, self).get_context_data(*args, **kwargs)
            print('Found')
            return context
        except MainPage.DoesNotExist:
            context['page'] =  Egg
            #TODO: send mail on error
            print('Not Found yet')
            return context
        return context
    
def contactView(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['subject']

        context = {'name':name, 'email': email, 'subject': subject, 'message': message}

        send_mail(
            subject,  #subject
            message, #message
            
            email, #from Email
           
            ['aamuhd9191@gmail.com'], #To Email
        )

        return render(request, 'core/contact.html')

    else:   


       return render(request, 'core/contact.html')
    
def user_profile(request, slug_id):

    profile = UserProfile.objects.get(slug=slug_id)
    context = {'profile': profile}
    return render(request, 'core/user.html', context)



def edit_profile(request, slug_id):

    
    profile = UserProfile.objects.get(slug=slug_id)
    #user = profile.user


    if request.method != 'POST':
        form = UserProfileForm(instance=profile)
    else:
        form = UserProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            
            
        return redirect('core:user', slug_id=slug_id)
    context = {'profile': profile, 'form': form}
    
    return render(request, 'core/editprofile.html', context)


@login_required(login_url='/account/login/')
def appointment(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        send_mail(
            subject,  #subject
            message, #message
            
            email, #from Email
           
            ['aamuhd9191@gmail.com'], #To Email
        )

        return redirect('core:home')

    else:   


       return render(request, 'core/appointment.html')



    

    
    

