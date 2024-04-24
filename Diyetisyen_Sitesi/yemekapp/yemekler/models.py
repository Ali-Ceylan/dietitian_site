from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from .utils import get_link_data
from datetime import datetime,date
from django.contrib.auth.models import *
from django.shortcuts import render

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Food(models.Model):
    
    category = models.ManyToManyField(Category, blank=True)
    yemek_adi = models.CharField(max_length=200,blank=True)
    aciklama = RichTextField(blank=True)
    resim = models.ImageField(upload_to="yemek_resim",blank=True)
    anasayfa = models.BooleanField(default=False)
    aktif = models.BooleanField(default=False)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    url = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.yemek_adi

    def save(self, *args, **kwargs):
        if self.url == "":
            self.slug = slugify(self.yemek_adi)
        else:
            tarif_adi, tarif_aciklama, tarif_resim = get_link_data(self.url)
            self.yemek_adi = tarif_adi
            self.aciklama = tarif_aciklama
            self.resim = tarif_resim
            self.slug = slugify(self.yemek_adi)
        super().save(*args, **kwargs)

class ContactForm(models.Model):
    name = models.CharField("İsim Soyisim", max_length=150)
    email = models.EmailField()
    subject = models.CharField("Konu", max_length=300)
    message = models.TextField("Mesaj", max_length=2000)
    created_at = models.DateTimeField("Gönderilme Tarihi", auto_now=True)

    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "İletişim Mesajları"
        verbose_name = "İletişim Mesajı" 
    
class Yorum(models.Model):
    
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.username} - {self.tarih}"


class Doktor(models.Model):
    ad = models.CharField(max_length=100)
    soyad=models.CharField(max_length=100)
    email = models.EmailField()
    uzmanlik_alani = models.CharField(max_length=100)

    def __str__(self):
        return self.ad
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ad)
        super().save(*args, **kwargs)
class pkategori(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Program Kategoriler"
        verbose_name = "Program Kategoriler" 
class Program(models.Model):
    pkategori = models.ManyToManyField(pkategori, blank=True)
    ad = models.CharField(max_length=100)
    icerik = models.TextField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    def __str__(self):
        return self.ad
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ad)
        super().save(*args, **kwargs)
class Randevu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser': False})
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    mesaj = models.TextField()
    saat=models.TimeField()
    tarih = models.DateField()
   
    class Meta:
        verbose_name_plural = "Randevular"
        verbose_name = "Randevular" 