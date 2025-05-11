from django.contrib import admin
from .models import Image_matieres, Epreuve, Logo_Ecole, Cours, Lecon, Niveau, Correction, Acheter,AcheterCorrect
# Register your models here.

admin.site.register(Logo_Ecole)
admin.site.register(Image_matieres)
admin.site.register(Epreuve)
admin.site.register(Cours)
admin.site.register(Lecon)
admin.site.register(Niveau)
admin.site.register(Correction)
admin.site.register(Acheter)
admin.site.register(AcheterCorrect)