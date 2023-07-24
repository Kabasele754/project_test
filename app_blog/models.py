from django.db import models

# Create your models here.


class Article:
    def __init__(self,title, description):
        self.title = title
        self.description = description
