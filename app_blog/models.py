from django.db import models

# Create your models here.
#  je suis un commentaire

class Article:
    def __init__(self,title, description):
        self.title = title
        self.description = description
