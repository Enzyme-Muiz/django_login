from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import miRNA
#from django.shortcuts import render
from .forms import UserForm, NewUserForm, ImageForm
from .methods import Allah
from .forms import *
from subprocess import run, PIPE, Popen
import sys
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

#def homepage(request):

	#return HttpResponse("I love <strong> my </strong> wife")
    #return HttpResponse(<a href="/3">Download</a>)
    #if request.method == POST:
    #	ww=request.POST['field']
    #	return render(request= request, 
    #	template_name= "main/home.html",
    #	context= {"mirna": miRNA.objects.all,
    #	"filled":ww}
    #	)

    #return render(request= request, 
    #	template_name= "main/home.html",
    #	context= {"mirna": miRNA.objects.all,
    #	"filled":3}
    #	)




def homepage(request):
    submitbutton= request.POST.get("submit")

    firstname=''
    lastname=''
    emailvalue=''
    number=''
    numberi=''
    another=''

    form= UserForm(request.POST or None)
    if form.is_valid():
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        number = form.cleaned_data.get("number")
        numberi= Allah(number)
        another = form.cleaned_data.get("another")
        

    context= {'form': form, 'firstname': firstname, 'lastname':lastname,
              'submitbutton': submitbutton, 'emailvalue':emailvalue, 
              'numberi': numberi, 'another': another}
        
    return render(request, 'main/home.html', context)
    




  
# Create your views here. 
def image_upload(request): 
    list_name= ["Mubaarak", "Nabeel", "Abdul-Mujeeb"]
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            send_mail("Received",
                "This is an automated email. Do not respond please",
                "muizdeenoyebode@gmail.com",
               ["oaonatraji@gmail.com", "muizdeenraji@gmail.com"],
               fail_silently= False )
            name= form.cleaned_data.get("name")
            messages.success(request, f" {name}")
            

            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'image_upload.html', {'form' : form, 'names': list_name}) 
def success(request): 
    return HttpResponse('successfully uploaded') 


def register(request):
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            username= form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")

            return redirect('homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    
    return render(request,
        'main/register.html',
        {'form': form}
        ) 
 

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("homepage")





def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user= authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('homepage')
            else:
                messages.error(request, "invalid username and password")
        else:
            messages.error(request, "invalid username and password")





    form = AuthenticationForm()
    return render(request,
        "main/login.html",
        {"form": form}
        )

    

def test(request): 
    return render(request, 'main/test.html') 




def execute(request):
    Input= request.POST.get("ok2")
    out= run([sys.executable, "C://Users//rajim//Desktop//django_app//mysite//tutorial.py", Input], shell= False, stdout=PIPE)
    out2= run([sys.executable, "C://Users//rajim//Desktop//django_app//mysite//BatchEffectRemoval2018-master/calibrate.py", 
              "--use_test", "--data_type", "cytof", "--data_path", "C:/Users/rajim/Desktop/django_app/mysite/uri", 
              "--model", "mlp", "--n_epochs", "20", "--experiment_name", "c15"], shell= False, stdout=PIPE)
    print(out)
    return render(request, 'main/test.html', {'out': out.stdout.decode('ascii')})
