from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.forms import UserForm, UserProfileInfoForm


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(req):

    return render(req, 'first_app/index.html')


def register(req):

    registered = False

    if req.method == 'POST':
        user_form = UserForm(data=req.POST)
        profile_form = UserProfileInfoForm(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            # HASH PASSWORD
            user.set_password(user.password)
            user.save()

            #grabs the profile form but does not save it
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            # save it to db
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm

    return render(req, 'first_app/registration.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def is_loggedIn(request):
    return HttpResponse('you are logged in')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('SOMEONE TRIED TO LOGIN AND FAIL')
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request, 'first_app/login.html')