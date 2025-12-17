from django.db import models
from django.utils import timezone


class Travailleurs(models.Model):
    STATUT_CHOICES = [
            ("CDI", "CDI"),
            ("CDD", "CDD"),
            ("Journalier", "Journalier"),
            ("Temporaire", "Temporaire"),
            ]


    ETAT_CHOICES = [
            ("Actif", "Actif"),
            ("Inactif", "Inactif"),
            ]


    matricule = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField(blank=True)
    section = models.CharField(max_length=100, blank=True)
    fonction = models.CharField(max_length=100, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="CDI")
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default="Actif")


    date_embauche = models.DateField(null=True, blank=True)
    date_debauche = models.DateField(null=True, blank=True)
    motif_de_debauche = models.TextField(blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["matricule", "nom"]


    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenom}"
    
class Absence(models.Model):
    TYPE_ABSENCE = [
        ('heure', 'Heure'),
        ('jour', 'Jour'),
    ]

    MOTIF_ABSENCE = [
        ('permission', 'Permission'),
        ('repos', 'Repos'),
        ('conge', 'Congé'),
        ('sansmotif', 'SansMotif'),
        ('autre', 'Autre'),
    ]

    travailleur = models.ForeignKey(Travailleurs, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    motif = models.CharField(max_length=50, choices=MOTIF_ABSENCE)
    type_absence = models.CharField(max_length=10, choices=TYPE_ABSENCE)
    duree = models.FloatField(help_text="Durée en heures ou en jours selon le type")

    def __str__(self):
        return f"{self.travailleur.nom} - {self.motif} - {self.type_absence} - {self.duree}"

class NightShift(models.Model):
    travailleur = models.ForeignKey(Travailleurs, on_delete=models.CASCADE,default=1  )
    date_debut = models.DateField()
    date_fin = models.DateField()

    """ class Meta:
        unique_together = ('travailleur', 'date_debut', 'date_fin')
 """
    def __str__(self):
        return f"{self.travailleur.nom} {self.travailleur.prenom} | {self.date_debut} → {self.date_fin}"

