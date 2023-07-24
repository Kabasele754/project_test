from django.shortcuts import render
from .models import Article

# Create your views here.


def indexView(request, template_name="blog/pages/index.html"):
    # context permet envoyer les codes python vers html
    # declaration de notre context
    context = {}
    bonjour = "Bonjour tout le monde ici c'est django"
    # affectaction la clef et valeur dans contex
    #          Key      Value

    # instance article
    a1 = Article("Java", "java description")
    a2 = Article("Python", "python description")
    a3 = Article("Django", "Django description")
    a4 = Article("C++", "C++ description")
    a5 = Article("C#", "C# description")
    a6 = Article("JavaScripts", "javaScripts description")
    a7 = Article("Dart", "Dart description")
    a8 = Article("Html", "Html description")
    list_article = [a1, a2, a3, a4, a5, a6,a7,a8]
    #
    for art in list_article:
        print(art.title)
    print(a1.title)
    context['name'] = bonjour
    context['article'] = list_article

    return render(request, template_name, context)
