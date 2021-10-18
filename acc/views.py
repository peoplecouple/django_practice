from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages
# Create your views here.


def index(request):
    messages.error(request, "에러발생!!")
    messages.warning(request, "경고!")
    messages.success(request, "성공!")
    messages.info(request,"정보!")
    return render(request, "index.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username") #"id" html태그에서 쓴거랑 맞춰야함
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('acc:index')
    return render(request, "acc/login.html")


def user_logout(request):
    logout(request)
    return redirect("acc:index")


def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username") #"id" html태그에서 쓴거랑 맞춰야함
        
        if User.objects.filter(username=username):
            messages.error(request, "동일 아이디가 존재합니다!")
            return redirect("acc:user_signup")
        password = request.POST.get("password")
        nickname = request.POST.get("nickname")
        comment = request.POST.get("comment")
        userpic = request.FILES.get("userpic")
            
        if not userpic:
            userpic = "media/usr/21/사진없음.jpg"
            messages.info(request, "사진이 기본값으로 설정되었습니다. 정보수정에서 사진을 넣어주세요.")
        User.objects.create_user(username=username, password=password, nickname=nickname, comment=comment, userpic=userpic).save()
        return redirect("acc:user_login") #가입 후 로그인으로 가게함
    return render(request, "acc/signup.html") 
    #등록하면 페이지가 있어야하니 리다이렉트 말고 렌더를함 안됨

def user_profile(request):
    return render(request, "acc/profile.html")
    
def update(request):
    user = request.user.username
    u = User.objects.get(username=request.user.username)
    if request.method == "POST" :
        p = request.POST.get("password")
        if p: #패스워드 없으면 빈칸되니까
            u.set_password(p) #비번은 암호화되야함
        u.nickname = request.POST.get("nickname")
        u.comment = request.POST.get("comment")
        up = request.FILES.get("userpic") #사진도 있으면 바꿔준다
        if up:
            u.userpic = up
        u.save()
        user_auth = authenticate(username=user, password=p)# 회원정보수정하면 기본세션끊김
        login(request, user_auth) # 다시 로그인 시키는거
        return redirect("acc:user_profile")

    return render(request, "acc/update.html")

def delete(request):
    User.objects.get(username=request.user.username).delete()
    return redirect('acc:user_login')

def assign(request):
    if not request.user.userpic:
        u = User.objects.get(username=request.user.username)
        u.userpic = "사진없음.png"
        u.save()
    return redirect("acc:index")