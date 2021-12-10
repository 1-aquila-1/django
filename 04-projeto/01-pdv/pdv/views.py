from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produto/index.html", context)