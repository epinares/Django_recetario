from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'cuentas/index.html') #cada vez que parta irá a buscar el html
