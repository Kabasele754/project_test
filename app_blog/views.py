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
    # SELECT * FROM Article; with SQL
    # With ORM
    list_article = Article.objects.all()

    context['name'] = bonjour
    context['article'] = list_article

    return render(request, template_name, context)
