from  django.urls import  path
from .views import  indexView, contactView, gestionContactView,\
    updateCotactView, deleteContactView


urlpatterns = [
    path('', indexView, name="index"),
    path('contact/', contactView, name='contact'),
    path('gestion-contact/', gestionContactView, name="gestion_contact"),
    path('gestion-contact/update/<int:contact_id>/', updateCotactView, name="update_contact"),
    path('gestion-contact/delete/<int:contact_id>/', deleteContactView, name="delete_contact")

]

