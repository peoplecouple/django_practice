from django.shortcuts import render, redirect
from .models import Quiz
from acc.models import User
# Create your views here.
def index(request):
    q = Quiz.objects.all()
    u = User.objects.all().order_by("-point")
    context = {
        'con' : q,
        'u' : u
    }
    return render(request, "quiz/index.html", context)

def judge(request, num):
    q = Quiz.objects.get(id=num)
    a = request.POST.get("answer")
    if q.answer == a:
        if not request.user in q.solver.all():
            q.solver.add(request.user)
            u = User.objects.get(username=request.user.username)
            u.point += q.point
            u.save()
    return redirect("quiz:index")