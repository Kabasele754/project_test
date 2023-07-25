from django.shortcuts import render
from .models import Article, Contact

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


def contactView(request, template_name="blog/pages/contact.html"):
    print("je veux voir le request", request)
    #  ici on verifie si la mathode de la request et == POST
    if request.method == "POST":
        # On recupere les valeurs entrer par l'utilisateur
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        print("je veux le nom", name)

        #  On creer notre Contact
        obj_contact = Contact(
            name= name,
            email= email,
            content = content
        )
        obj_contact.save()





    return render(request, template_name)