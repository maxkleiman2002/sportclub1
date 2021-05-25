from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'context_var': 'test'
    }
    return render(request, 'index.html', context=context)
