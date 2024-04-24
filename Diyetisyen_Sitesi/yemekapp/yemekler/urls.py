from django.urls import path
from . import views
from . import models
from django.urls import path
from .views import *

urlpatterns = [
    path('iletisim', views.iletisim, name='iletisim'),
    path('mail_formu', views.mail_gonder, name='mail_gonder'),
    path('mail', views.email, name='mail'),
    path('mail_formu', views.ContactFormView.as_view(), name='mail_gonder'),
    path("", views.home, name = "home"),
    path("Anasayfa", views.home),
    path("diyet",views.diyet, name = "diyet"),
    path("prodetay",views.prodetay, name = "prodetay"),
    path("prodetay2",views.prodetay2, name = "prodetay2"),
    path("prodetay3",views.prodetay3, name = "prodetay3"),
    path("prodetay4",views.prodetay4, name = "prodetay4"),
    path("programlar",views.programlar, name = "programlar"),
    path("doktorlar",views.doktorlar, name = "doktorlar"),
    path("yemekler", views.yemekler, name = "yemekler"),
    path("yemekler/<slug:slug>", views.yemekdetails, name = "details"),
    path("kategori/<slug:slug>",views.yemekcategory, name  = "yemekcategory"),
    path('yorumlar/',views.yorumlar, name='yorumlar'),
    path('kullanicilar/', views.kullanici_listesi, name='kullanicilar'),
    path("yemekler", views.yemekler, name = "yemekler"),
    path("randevu_al", views.randevular, name = "randevu_al"),
    path("vucutkitle", views.vucutkitle, name = "vucutkitle"),
    path("bazal", views.bazal, name = "bazal"),
    path("vucutyag", views.vucutyag, name = "vucutyag"),
    path("idealkilo", views.idealkilo, name = "idealkilo"),
    path("gunlukkalori", views.gunlukkalori, name = "gunlukkalori"),
    path("diyetisyenler", views.diyetisyenler, name = "diyetisyenler"),
]