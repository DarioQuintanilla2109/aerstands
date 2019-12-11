from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from lessors.models import Lessor
from lessees.models import Lessee
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def signup(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        company = request.POST['company']
        signed_as = request.POST['signup_as']

        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords must match')
            return redirect('signup')
        # Check if email exists already
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'That email is already being used')
            return redirect('signup')
        else:
            # Looks good
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name,
                                            email=email, password=password)
            # Login after register
            user.save()
            # create a Lessor if user signed up as a lessor
            if signed_as == 'Lessor':
                lessor = Lessor.objects.create(connect_id='', first_name=first_name,
                                               last_name=last_name, company=company,
                                               email=email)
            # create a Lessee if user signed up as a lessee
            else:
                lessee = Lessee.objects.create(connect_id='', first_name=first_name,
                                               last_name=last_name, company=company,
                                               email=email)
            messages.success(request, 'You are now signed up and can log in')
            return redirect('login')

    return render(request, 'accounts/signup.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            lessors = Lessor.objects.filter(email=email)
            lessees = Lessee.objects.filter(email=email)
            if lessors:
                return redirect('lessor_dashboard')
            elif lessees:
                return redirect('lessee_dashboard')
        else:
            messages.error(request, 'Invalid email/password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')

def lessor_dashboard(request):
    lessors = Lessor.objects.filter(email=request.user.email)

    context = {
        'lessors': lessors
    }
    return render(request, 'accounts/lessor_dashboard.html', context)

def lessee_dashboard(request):
    lessees = Lessee.objects.filter(email=request.user.email)

    context = {
        'lessees': lessees
    }
    return render(request, 'accounts/lessee_dashboard.html', context)
