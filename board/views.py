from django.shortcuts import redirect, render
from .models import Board, Reply
from django.core.paginator import Paginator #pg와 관련됨
from django.utils import timezone
from django.contrib import messages
# Create your views here.


def index(request):
    page = request.GET.get('page', 1) #page가 없으면 1로 두겠다 의미
    kw = request.GET.get('kw', '')
    cate = request.GET.get('cate', '')
    if kw:
        if cate == 'Subject':
            b = Board.objects.filter(subject__contains = kw).order_by("-c_time")
        if cate == 'Writer':
            b = Board.objects.filter(writer__contains = kw).order_by("-c_time")
        else:
            b = Board.objects.filter(content__contains = kw).order_by("-c_time")
    else:
        b = Board.objects.order_by("-c_time") #현재 100개 넘게 글이 있음
    pag = Paginator(b,10)  #b 줄께 10개씩 묶어줘
    obj = pag.get_page(page) #1페이지 가져와라 2넣으면 pg2나오고 10넣으면 pg10나옴
    context = {
        'con': obj,
        'kw' : kw,
        'cate' : cate,
    }
    return render(request, "board/index.html", context)

def detail(request, num):
    try:
        b = Board.objects.get(id=num)
        r = b.reply_set.all() #리플 다 갖고오겠따
        context = {
            'con': b,
            'rep': r,
        }
    except:
        return render(request, "error/notfound.html")
    return render(request, "board/detail.html", context)

def create(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        writer = request.user.username
        content = request.POST.get("content")
        Board(subject=subject, writer=writer, content=content, likey=0, c_time=timezone.now()).save()
        return redirect("board:index")

    return render(request, "board/create.html")

def delete(request, conid):  
    try:
        b = Board.objects.get(id=conid)
        if b.writer == request.user.username:
            b.delete()
        else:
            messages.warning(request, "본인만 삭제 가능합니다.")
            return render(request, "error/forbidden.html")
    except:
        messages.warning(request, "게시물이 없습니다.")
        return render(request, "error/notfound.html")
    return redirect("board:index")

def update(request, conid):
    b = Board.objects.get(id=conid)
    if request.user.username == b.writer:
        if request.method == "POST":
            b.subject = request.POST.get("subject")
            b.content = request.POST.get("content")  #바뀌는 부분만 바꿔서 세이브하기
            b.save()
            return redirect("board:detail", num=conid)
        context = {
            'con' : b
        }
        return render(request, "board/update.html", context)
    else:
        return render(request, "error/forbidden.html")

def create_reply(request, conid):
    b = Board.objects.get(id=conid) #외래키니까 참조하는거 부터 갖고오기
    r = request.user.username
    c = request.POST.get('comment')
    p = request.user.userpic
    Reply(subject=b, replyer=r, comment=c, pic=p).save()
    return redirect("board:detail", num=conid)

def delete_reply(request, conid, num):
    r= Reply.objects.get(id=num)  #게시판 번호의 댓글을 가져온다
    if request.user.username == r.replyer: #댓글쓴이와 유저가 같으면 삭제가능
        r.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect("board:detail", num=conid)
    
def up(request, conid):
    b = Board.objects.get(id=conid) 
    if request.user in b.up.all(): #좋아요 했으면 바로 리턴
        return redirect("board:detail", num=conid)
    b.up.add(request.user) #투표한 유저에 넣어줌
    return redirect("board:detail", num=conid) 

def cancel(request, conid):
    b = Board.objects.get(id=conid) 
    if request.user in b.up.all(): 
        b.up.remove(request.user)    
    return redirect("board:detail", num=conid) 
