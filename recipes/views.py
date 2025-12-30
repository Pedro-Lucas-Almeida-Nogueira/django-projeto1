from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',context={
        'name':'Pedro'
    },status=201)
