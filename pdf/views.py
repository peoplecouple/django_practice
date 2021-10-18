from django.shortcuts import render
import pdfplumber
# Create your views here.

def plum_daldal(filename):
    text=""  
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text += page.extract_text()
    return text

def index(request):
    context={}
    if request.method == "POST":
        pdf = request.FILES.get("file")
        context.update({
            "con" : plum_daldal(pdf)
        })
    return render(request, "pdf/index.html", context)



