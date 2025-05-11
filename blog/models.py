from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Logo_Ecole(models.Model):
    titre_ecole=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image_logo_ecole/')

    
    def __str__(self):
        return self.titre_ecole


class Image_matieres(models.Model):
    nom = models.CharField(max_length=500)
    image=models.ImageField(upload_to='image_matiere/')
    def __str__(self):
        return self.nom

class  Niveau(models.Model):
    nom = models.CharField(max_length=500)
    def __str__(self):
        return self.nom

class Epreuve (models.Model):
    nom = models.CharField(max_length=500)
    niveau =models.ForeignKey(Niveau, on_delete=models.CASCADE, null=True)
    ecole =models.ForeignKey(Logo_Ecole, on_delete=models.CASCADE, null=True)
    image=models.ForeignKey(Image_matieres, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdfs_epreuve/')
    date_consultation = models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_epreuve = models.ImageField(upload_to='photo_epreuve', null=True)
    def __str__(self):
        return self.nom
    
class Correction (models.Model):
    nom = models.CharField (max_length=100)
    pdf = models.FileField(upload_to='pdfs_epreuve/')
    image_apercu = models.ImageField(upload_to='apercu_image_correction', null=True)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    niveau=models.ForeignKey(Niveau, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image_matiere/')
    date_consultation = models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre
    
class Lecon(models.Model):
    titre = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs_cours/')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titre

class Acheter (models.Model):
    acheteur = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE,null=True)
    date_consultation = models.DateTimeField(auto_now_add=True, null=True)

class AcheterCorrect (models.Model):
    acheteur = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    correction = models.ForeignKey(Correction, on_delete=models.CASCADE,null=True)
    date_consultation = models.DateTimeField(auto_now_add=True, null=True)