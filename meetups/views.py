from django.shortcuts import redirect, render
from .models  import Meetup, Participants
from .form import RegistrationForm
# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html', {
       'meetup' : meetups
    })
    
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method  == 'GET': 
            
            registration_form = RegistrationForm()
            
        else:
            registration_form = RegistrationForm(request.POST)  
            if registration_form.is_valid():
               user_email = registration_form.cleaned_data['email']
               participante, _  = Participants.objects.get_or_create(email=user_email)
               selected_meetup.participant.add( participante)
               return redirect('registration_succesful', meetup_slug=meetup_slug)
           
        return render(request, 'meetups/meetup_details.html', {
                'meetup_found' : True,    
                'meet_up' : selected_meetup,
                'form' : registration_form
            }) 
               
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup_details.html', {
             'meetup_found' : False  }  ) 
        
        
        
def registration_succesful(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return  render(request, 'meetups/registration_succesful.html', {'organizer_mail' : meetup.organizer_email})            