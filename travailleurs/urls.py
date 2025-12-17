from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='travailleurs/login.html'), name='login'),  # la racine = login
    path('logout', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('travailleurs/', views.travailleur_list, name='travailleur_list'),
    path('travailleurs/export_excel', views.export_travailleurs_excel, name='export_travailleurs_excel'),
    path('travailleurs/create/', views.travailleur_create, name='travailleur_create'),
    path('travailleurs/<int:pk>/', views.travailleur_detail, name='travailleur_detail'),
    path('travailleurs/<int:pk>/update/', views.travailleur_update, name='travailleur_update'),
    path('travailleurs/<int:pk>/delete/', views.travailleur_delete, name='travailleur_delete'),
    path('absences/', views.liste_absences, name='liste_absences'),
    path('absences/creer/', views.creer_absence, name='creer_absence'),
    path('absences/modifier/<int:pk>/', views.modifier_absence, name='modifier_absence'),
    path('absences/supprimer/<int:pk>/', views.supprimer_absence, name='supprimer_absence'),
    path('nightshift/', views.liste_nightshift, name='liste_nightshift'),
    path('nightshift/creer/', views.creer_nightshift, name='creer_nightshift'),
    path('nightshift/supprimer/<int:pk>/', views.supprimer_nightshift, name='supprimer_nightshift'),
    path('etat_presence/', views.etat_presence, name='etat_presence'),
    path("export_presence_excel/", views.export_presence_excel, name="export_presence_excel"),
    path("absences/export_excel/", views.export_absences_excel, name="export_absences_excel"),


]
