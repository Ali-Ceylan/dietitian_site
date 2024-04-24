from django.contrib import admin
from .models import *
from .models import Doktor, Program
from django.utils.safestring import mark_safe



class YemekAdmin(admin.ModelAdmin):
    list_display = ("yemek_adi","anasayfa","aktif","secili_kategoriler","olusturma_tarihi","guncelleme_tarihi","slug",)
    list_editable = ("anasayfa","aktif",)
    search_fields = ("yemek_adi","aciklama")
    readonly_fields = ("slug",)
    list_filter = ("anasayfa","aktif","category",)

    def secili_kategoriler(self, obj):
        html = "<ul>"
        
        for i in obj.category.all():
            html += "<li>" + i.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('ad',"kategori","slug")
    list_filter = ("pkategori",)
    def kategori(self, obj):
        html = "<ul>"
        
        for i in obj.pkategori.all():
            html += "<li>" + i.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    fieldsets = (
        ("MESAJLAR", {
            "fields": ("name", "email", "subject", "message", "created_at")
        }),
    )
    
class Doktoradmin(admin.ModelAdmin):
    list_display=("ad","uzmanlik_alani")

class randevuadmin(admin.ModelAdmin):
    list_display=("doktor","saat","tarih","mesaj")

class categoryduzenle(admin.ModelAdmin):
    list_display = ("name","slug",)
    readonly_fields =("slug",)
   
admin.site.register(Category, categoryduzenle)
admin.site.register(Food, YemekAdmin)
admin.site.register(Yorum)
admin.site.register(ContactForm)  
admin.site.register(Doktor,Doktoradmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(pkategori)
admin.site.register(Randevu,randevuadmin)