from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm
from .models import Signup  # (Assuming you have a Signup model)

# global variable

user=''
def homepage(request):
    context={
        'user':user,
    }
    return render(request, 'ui/homepage.html', context=context)

def success(request):
    context={}
    return render(request, 'auth/success.html', context=context)

def signup(request):
    error=""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            email = cleaned_data['email']
            password = cleaned_data['password']
            confirm_password = cleaned_data['confirm_password']
            if  password and confirm_password and password != confirm_password:
                error="Passwords do not match"
                return render(request, 'auth/signup.html', {'error':error})
            else:
                form.save()
        # get the form data
            print(f"username:{username} \n email: {email}\n password: {password} \n confirm password:{confirm_password}")
        # redirect to successpage
            return redirect("success")

        else:
            pass
    else:
        form = SignupForm()

    context = {'form': form,
               'error':error}
    return render(request, 'auth/signup.html', context)

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        entered_password = request.POST.get('password')
        try:
            user=Signup.objects.get(email=email)
            password=user.password
            if entered_password==password:
                print("SuccessFull")
                print(f"User: {user}")
                print(f"email: {email}\n Password: {password}\nEnterpassword: {entered_password}")
                context = {
                    "user": user
                }
                return redirect('user', username=user)
            else:
                return render(request, 'auth/invalid.html')

        except Signup.DoesNotExist:
            return render(request, 'auth/invalid.html')
    context = {}
    return render(request, 'auth/loginpage.html', context=context)

def user(request, username):
    context = {
        'user': user,
        'username':username,
    }
    print(f"frome userpage: {user}")
    return render(request, 'auth/userpage.html', context=context)


