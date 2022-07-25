from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        u = request.POST['user'],
        p = request.POST['pass']
        user = authenticate(request, username=u, password=p)
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('/asosiy/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        if request.method == 'POST':
            u = User.objects.create_user(
                n = request.POST['name'],
                l_n=request.POST['last_name'],
                e=request.POST['email'],
                c=request.POST['city'],
                p = request.POST['pass']
            )
            return redirect('login')
