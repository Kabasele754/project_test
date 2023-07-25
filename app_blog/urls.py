from  django.urls import  path
from .views import  indexView, contactView


urlpatterns = [
    path('', indexView, name="index"),
    path('contact/', contactView, name='contact')

]

