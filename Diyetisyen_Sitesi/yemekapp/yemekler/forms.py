from django import forms
from django.forms import ModelForm,DateInput
from django.contrib.auth.models import User
from .models import *
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from datetime import time, datetime


class ContactmeForm(forms.ModelForm):
    

    class Meta:
        model = ContactForm
        fields = ["email", "subject", "message"]  
    email = forms.ModelChoiceField(
        queryset=User.objects.filter(is_superuser=False).values_list('email', flat=True),
        label='E-Posta',
        empty_label='E-Posta Seçiniz',
    )

class YorumFormu(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['icerik']
    icerik =forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mesajınızı buraya yazabilirsiniz'}))

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Randevu
        fields = ['doktor', 'saat', 'tarih', 'mesaj']

    # Doktor seçim alanını özelleştirmek için ModelChoiceField kullanılmış
    doktor = forms.ModelChoiceField(
        queryset=Doktor.objects.all(),
        label='Dyt',
        empty_label='Diyetisyen Seçiniz',
    )

    # Saat giriş alanını özelleştirmek için TimeField kullanılmış
    saat = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}),help_text='Saat seçiniz')

    # Tarih giriş alanını özelleştirmek için DateField kullanılmış
    tarih = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),help_text='Tarih seçiniz')

    # Mesaj giriş alanını özelleştirmek için CharField ve Textarea kullanılmış
    mesaj = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mesajınızı buraya yazabilirsiniz'}))

    # Saat alanını temizleme (clean) işlemi
    def clean_saat(self):
        saat = self.cleaned_data.get('saat')
        if saat is not None and (saat < time(8, 0) or saat > time(18, 0)):
            raise forms.ValidationError("Lütfen geçerli bir saat girin (08:00 - 18:00 arası)")
        return saat

    # Tarih alanını temizleme (clean) işlemi
    def clean_tarih(self):
        tarih = self.cleaned_data.get('tarih')
        today = datetime.now().date()
        if tarih is not None and tarih < today:
            raise forms.ValidationError("Geçmiş bir tarih seçemezsiniz")
        return tarih 
