from django.shortcuts import render, redirect
from django.contrib import messages
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
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # Utilisation du context
    context["contacts"] = contacts

    #  ici la condition on verifie si la mathode de la request et == POST
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

    return render(request, template_name, context)


def gestionContactView(request, template_name="blog/pages/gestion_contact.html"):
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # Utilisation du context
    context["contacts"] = contacts
    #  ici la condition on verifie si la mathode de la request et == POST
    if request.method == "POST":
        # On recupere les valeurs entrer par l'utilisateur

        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        print("je veux le nom", name)

        #  On creer notre Contact
        obj_contact = Contact(
            name=name,
            email=email,
            content=content
        )
        obj_contact.save()

    return render(request, template_name, context)

# fonction  update

def updateCotactView(request,contact_id, template_name="blog/pages/gestion_contact.html"):
    contact_one = Contact.objects.get(id=contact_id)
    print("id", contact_one)
    context = {}
    contacts = Contact.objects.all()
    context['contacts'] = contacts
    context['contact_one'] = contact_one
    #  la condition == post
    if request.method == "POST":
        # recuper les donnees qui se trouve dans input et on le modifie
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        #  assign de valeurs input
        contact_one.name = name
        contact_one.email = email
        contact_one.content = content
        # on sauvegarde la modification
        contact_one.save()

    return render(request, template_name, context)


def deleteContactView(request, contact_id):
    contact_one = Contact.objects.get(id=contact_id)
    contact_one.delete()

    return redirect('gestion_contact')
