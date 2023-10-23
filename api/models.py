from django.db import models
from django.contrib.auth.models import User
import uuid

class Supermarket(models.Model):
    supermarket = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    nom_drive = models.CharField(max_length=255)
    nom_driveUrl = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=7, null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=7, null=True)
    lien_drive = models.CharField(max_length=255, blank=True)
    dateScraped = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table='supermarket'
    def __str__(self):
        return self.nom_drive

class Product(models.Model):
    
    supermarket = models.CharField(max_length=255, null=True, blank=True)
    nom_drive = models.CharField(max_length=255, null=True, blank=True)
    nom_driveUrl = models.CharField(max_length=255, blank=True)
    rayon_principal = models.CharField(max_length=255)
    rayon_secondaire = models.CharField(max_length=255)
    nom_produit = models.CharField(max_length=255)
    prix_produit = models.DecimalField(max_digits=10, decimal_places=2)
    prix_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unite = models.CharField(max_length=255, null=True, blank=True)
    lien_image = models.URLField(max_length=255, null=True, blank=True)    
    class Meta:
        managed = False
        db_table='product'
    def __str__(self):
        return self.nom_produit
    
