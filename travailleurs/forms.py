from django import forms
from .models import Travailleurs
from .models import Absence

class TravailleursForm(forms.ModelForm):
    class Meta:
        model = Travailleurs
        fields = '__all__'
        widgets = {
            'date_embauche': forms.DateInput(attrs={'type': 'date'}),
            'date_debauche': forms.DateInput(attrs={'type': 'date'}),
            'adresse': forms.Textarea(attrs={'rows': 2}),
            'motif_de_debauche': forms.Textarea(attrs={'rows': 2}),
        }
from django.forms import DateInput

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['travailleur', 'motif','date', 'type_absence', 'duree']
        widgets = {
            'travailleur': forms.Select(attrs={'class': 'form-control'}),
            'motif': forms.Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'type_absence': forms.Select(attrs={'class': 'form-control'}),
            'duree': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }

from django import forms

class NightShiftForm(forms.Form):
    date_debut = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_fin = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    travailleurs = forms.ModelMultipleChoiceField(
        queryset=Travailleurs.objects.filter(etat='Actif'),
        widget=forms.CheckboxSelectMultiple
    )

class PeriodeForm(forms.Form):
    date_debut = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))