from django.shortcuts import render


# Create your views here.
def splash_page(request):
    return render(request, 'splashpage.html')
