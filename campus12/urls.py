"""campus12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',accueil,name="accueil"),
    path('epreuve/logo ecole',epreuve,name="epreuve-correction"),
   
    path('cours',cours,name="cours"),
    path('cours/Lecons<int:id_cours>',lecons,name="lecons"),
    path('Politique_de_confidentialite',politique,name="politique"),
    path('Cours_de_soutien',soutien,name="soutien"),
    path('Commande_bord',bord,name="bord"),
    path('traitement',traitement,name="traitement"),
    path('authentification/', include('app_auth.urls')),
    
    path('contact',contact,name="contact"),
    path('epreuve/logo ecole/detail/<int:id_logo_ecole>/', detail, name='detail'),
    path('epreuve/logo ecole/ detail/message',message,name="message"),
    path('epreuve/apercu/<int:id_selection_epreuve>/',apercu,name="apercu"),
    path('correction',correction, name='correction'),
    path('dashboard/epreuve&correction',dashboard, name='dashboard'),
    path('dashboard/achat',dashboard_achat, name='dashboard_achat'),
    path('correction/apercu_correction/<int:correction_id>/', apercu_correction, name='apercu_correction'),
    path('epreuve/paiement/<int:epreuve_id>/', paiement, name='paiement'),
    path('epreuve/telechargement/<int:epreuve_id>/', telechargement, name='telechargement'),
    path('correction/paiement_correction/<int:correction_id>/',paiement_correction, name='paiement_correction'),
    path('correction/telechargement_correction/<int:correction_id>/',telechargement_correction, name='telechargement_correction'),
    path('epreuve&correction/dashboard/recherche',recherche_dashboard,name='recherche_dashboard'),
    path('correction/recherche', recherche_correction, name='recherche_correction'),
    path('epreuve/recherchee', recherche_epreuve, name='recherche_epreuve'),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'https://1stsss.com/wp-content/uploads/2015/02/C12-logo.jpg   lien du logo'