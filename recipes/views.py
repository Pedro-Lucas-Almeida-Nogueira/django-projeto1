from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html',context={
        'name':'Pedro'
    },status=201)

def outro(request, id):
    return render(request, 'recipes/pages/outro.html',context={
        'name':'Pedro'
    },status=201)