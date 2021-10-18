from django.shortcuts import render
from googletrans import Translator

# Create your views here.

def index(request):
    context = {}
    if request.method =="POST":
        text = request.POST.get('before')
        if text: #입력안하면 아무일도 안생김
            f = request.POST.get('from')
            t = request.POST.get('to')
            translator = Translator()
            if not f or not t:
                trans = translator.translate(text, dest="ko")
            else:
                trans = translator.translate(text, src=f, dest=t)
            context.update({ #업데이트는 키 여러개 포스트 겟 상관없음
                'before' : text,
                'after' : trans.text,
                'from' : f,
                'to' : t,
            })
    return render(request, "translator/index.html", context)