import io
import json
import time
import os

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import SignupForm
from .models import Signup, ContactUs, UserData  # Assuming you have a Signup model
import speech_recognition as sr
from django.shortcuts import render
from django.http import JsonResponse

user = ''

def homepage(request):
    context = {
        'user': user,
    }
    return render(request, 'ui/homepage.html', context=context)

def about_page(request):
    return render(request, 'ui/about.html', {})

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"{name}  {email}  {message}")
        userInput = ContactUs.objects.create(name=name, email=email, message=message)
        userInput.save()

        time.sleep(3)
        return render(request, 'ui/contact.html', {})
    return render(request, 'ui/contact.html', {})

def success(request):
    context = {}
    return render(request, 'auth/success.html', context=context)

def signup(request):
    error = ""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            email = cleaned_data['email']
            password = cleaned_data['password']
            confirm_password = cleaned_data['confirm_password']
            if password and confirm_password and password != confirm_password:
                error = "Passwords do not match"
                return render(request, 'auth/signup.html', {'error': error})
            else:
                form.save()
                # get the form data
                print(f"username:{username} \n email: {email}\n password: {password} \n confirm password:{confirm_password}")
                # redirect to success page
                return redirect("success")

        else:
            pass
    else:
        form = SignupForm()

    context = {'form': form,
               'error': error}
    return render(request, 'auth/signup.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        entered_password = request.POST.get('password')
        try:
            user = Signup.objects.get(email=email)
            password = user.password
            if entered_password == password:
                print("Successful")
                print(f"User: {user}")
                print(f"email: {email}\n Password: {password}\nEnterpassword: {entered_password}")
                context = {
                    "user": user
                }
                return redirect('user', username=user.username)
            else:
                return render(request, 'auth/invalid.html')

        except Signup.DoesNotExist:
            return render(request, 'auth/invalid.html')
    context = {}
    return render(request, 'auth/loginpage.html', context=context)

def user(request, username):
    if request.method == 'POST':
        recognizer = sr.Recognizer()
        audio_file = request.FILES.get('audio')
        real_time_transcription = request.POST.get('real_time_transcription')

        if audio_file:
            # Save the uploaded file to a specific folder
            audio_path = os.path.join('media', 'audio', audio_file.name)
            print(audio_path)
            with open(audio_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Process the saved audio file
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)
                print(audio_data)
                try:
                    text = recognizer.recognize_google(audio_data)
                    return render(request, 'ui/output.html', {'text': text, 'username': username})
                except sr.UnknownValueError:
                    return JsonResponse({'error': 'Speech not recognized'})
                except sr.RequestError:
                    return JsonResponse({'error': 'API unavailable'})

        elif real_time_transcription:
            # Handle real-time transcription
            return render(request, 'ui/output.html', {'text': real_time_transcription, 'username': username})

    return render(request, 'auth/userpage.html', {'text': '', 'username': username})



def microphone_input(request, username):
    if request.method == 'POST':
        # Retrieve the transcript from the POST data
        transcript = request.POST.get('result')
        print('*' * 67)
        print('Received transcript:', transcript)
        print('*' * 67)

        # Ensure the directory exists
        directory = os.path.join('media', 'transcript')
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, f'{username}_transcription.txt')
        print(file_path)

        # Write the transcript to the file
        try:
            with open(file_path, 'a') as file:
                file.write(transcript + "\n")
        except IOError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        userObj=Signup.objects.get(username=username)
        # Get the user associated with the given username
        user = get_object_or_404(Signup, email=userObj.email)

        # Save the transcript file path to the UserData model
        with open(file_path, 'rb') as file:
            content = ContentFile(file.read())
            user_data = UserData(email=user)
            user_data.activity.save(f'{username}_transcription.txt', content)
            user_data.save()

        # Return a JSON response
        return JsonResponse({'status': 'success', 'message': 'Text stored successfully'})

    # For GET requests or other methods, render the form page
    return render(request, 'ui/microphone_input.html', {'username': username})



def output(request, username):
    return render(request, 'ui/output.html', {'text': '', 'username': username})
