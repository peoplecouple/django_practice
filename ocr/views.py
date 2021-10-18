from django.shortcuts import render
import pytesseract
from PIL import Image #이미지 라이브러리랑 같이 써야함
# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        pic = request.FILES.get("pic")
        nat = request.POST.get("nat")
        pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
        img = Image.open(pic)
        text = pytesseract.image_to_string(img, lang=nat)
        context.update({
            "con" : text,
            "nat" : nat
        })
    return render(request, "ocr/index.html", context)


