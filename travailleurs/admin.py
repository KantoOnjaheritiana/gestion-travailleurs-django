from django.contrib import admin
from .models import Travailleurs


@admin.register(Travailleurs)
class TravailleursAdmin(admin.ModelAdmin):
    list_display = ("matricule", "nom", "prenom", "section", "fonction", "statut", "etat", "date_embauche")
    list_filter = ("section", "statut", "etat")
    search_fields = ("matricule", "nom", "prenom", "section")
