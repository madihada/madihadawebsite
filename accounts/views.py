from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '아이디가 이미 사용되었습니다!')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '메일주소가 이미 사용되었습니다!')
            else:
                user = User.objects.create_user(username = username, email=email, password=password1)
                user.save();
                messages.info(request, '아이디가 생성되었습니다!')
                return redirect('/')
        else:
            messages.info(request, '비밀번호를 확인해주세요!')

    return render(request, 'signup.html')

