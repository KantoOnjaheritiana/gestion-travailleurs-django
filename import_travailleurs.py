import os
import django
import openpyxl
from datetime import datetime

# Config Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion_travailleurs.settings")
django.setup()

from travailleurs.models import Travailleurs

# Chemin relatif : fichier à côté de manage.py
excel_file = "travailleurs.xlsx"

# Ouvrir le fichier Excel
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

# Boucle sur chaque ligne à partir de la 2e (en-tête)
for row in sheet.iter_rows(min_row=2, values_only=True):
    matricule, nom, prenom, adresse, section, fonction, statut, etat, date_embauche, date_debauche, motif_de_debauche = row

    # Ignorer si matricule vide
    if not matricule:
        continue

    # Valeurs par défaut si vide
    nom = nom or "Inconnu"
    prenom = prenom or ""
    statut = statut or "CDI"
    etat = etat or "Actif"
    adresse = adresse or ""
    section = section or ""
    fonction = fonction or ""
    motif_de_debauche = motif_de_debauche or ""

    # Convertir les dates si nécessaire
    if isinstance(date_embauche, datetime):
        date_embauche = date_embauche.date()
    if isinstance(date_debauche, datetime):
        date_debauche = date_debauche.date()

    # Créer ou mettre à jour le travailleur
    obj, created = Travailleurs.objects.update_or_create(
        matricule=matricule,
        defaults={
            'nom': nom,
            'prenom': prenom,
            'adresse': adresse,
            'section': section,
            'fonction': fonction,
            'statut': statut,
            'etat': etat or "Actif",  # <-- important
            'date_embauche': date_embauche,
            'date_debauche': date_debauche,
            'motif_de_debauche': motif_de_debauche
        }
    )

    print(f"{'Créé' if created else 'Mis à jour'} : {matricule} - {nom} {prenom}")

print("Import terminé ✅")
