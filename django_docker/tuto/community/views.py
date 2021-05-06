from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .forms import Form
from .models import Article

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Form()
    return render(request, 'write.html', {'form': form, 'name':'Joon Ho'})

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList': articleList})

def view(request, num):
    article = Article.objects.get(id = num)
    return render(request, 'view.html', {'article': article})

@api_view(['GET'])
def helloAPI(request):
    article = Article.objects.get(id = 1)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)