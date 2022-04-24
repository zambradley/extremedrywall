from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def aboutUs(request):
    context={}
    return render(request, 'aboutus.html', context)

def paint(request):
    context={}
    return render(request, 'paint.html', context)

def tape(request):
    context={}
    return render(request, 'tape.html', context)

def texture(request):
    context={}
    return render(request, 'texture.html', context)

def hang(request):
    context={}
    return render(request, 'hang.html', context)

def service(request):
    context={}
    return render(request, 'services.html', context)

def careers(request):
    context={}
    return render(request, 'careers.html', context)

def admin(request):
    context={}
    return render(request, 'admin.html', context)

def contact(request):
    context={}
    return render(request, 'contact.html', context)
