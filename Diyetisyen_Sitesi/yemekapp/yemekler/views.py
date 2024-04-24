from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .models import ContactForm
from django.views.generic import ListView,FormView
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import ContactForm
from django.http import HttpResponseRedirect

def home(request):
    data = {
        "yemekler": Food.objects.filter(anasayfa=True, aktif=True),
        "kategoriler": Category.objects.all(),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
    return render(request, "index.html", data)

def diyet(request):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
    return render(request, "diyet.html", data)
def iletisimmesajlari(request):
    data = {
        "mesajlar": ContactForm.objects.all(),
        }
    return render(request, "mail_formu.html", data)

def yemekler(request):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(aktif=True),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
    return render(request, "yemekler.html", data)

def yemekcategory(request, slug):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(category__slug=slug),
        "secilen_kategori": slug,
        }
    return render(request, "yemekler.html", data)

def doktorlar(request):
    data = {
        "doktorlar": Doktor.objects.all(),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        
        }
    return render(request, "diyetisyenler.html", data)

def programlar(request):
    data = {
        
        "programlar": Program.objects.all(),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
    return render(request, "programlar.html", data)

class ContactFormView(FormView):
    template_name = 'iletisim.html'
    form_class = ContactmeForm
    success_url = '/'
    model=ContactForm

    def form_valid(self, form,request):
        name="Diyetisyen Merkezi"
        my_subject="diyet"
        my_message="Kilo verme,Kilo alma kolay paketi:"
        "KAHVALTI-->Baharatlı haşlanmış yumurta,lor peyniri|"
        "1.Ara Öğün:Yulaf Topları,Kırmızı Elma|"
        "Öğle Yemeği:Fırında Tavuk But,Pirinç Pilavı,Enginar Kalbi Salatası|"
        "2.Ara Öğün:Karabuğday patlağıüzerine şekersiz fıstık ezmesi,Muz,Tatlı lor|"
        "Akşam Yemeği:Izgara Biftek,Domates Soslu Makarna,Fırında brüksel lahanası (nar ve ceviz eşliğinde)|"
        "Antreman Sonrası:Magic Smoothie,Ton balıklı sandviç"                                                   
        my_email="diyetisyenmerkezi12@gmail"
        from_email=None,
        fail_silently=False
    
        
        obj=ContactForm(
            name="Diyetisyen Merkezi",
            subject=my_subject,
            message=my_message,
            email=my_email
        ) 
        obj.save()
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject ']
        message = form.cleaned_data['message']
        email = form.cleaned_data['mail']
        
        if request.method == 'POST':
            subject =my_subject
            message = my_message
            email = my_email
            alici = request.POST['alici']

        # E-posta gönderme işlemi
            send_mail(subject, message, email, [alici])

            return HttpResponseRedirect('/iletisim')  # E-posta gönderme başarılıysa yönlendirilecek sayfa
        form.save() 
        return render(request, '/mail_formu.html')
def mail_gonder(request):
    my_konu=request.POST['konu']
    my_kahvalti=request.POST['kahvalti']
    my_ogle_yemegi=request.POST['ögle_yemegi']
    my_aksam_yemegi=request.POST['aksam_yemegi']
    my_icerik=request.POST['içerik'] 
    my_alici = request.POST['email']                                        
    my_gonderen="diyetisyenmerkezi12@gmail"

    kahvalti_program = Program.objects.get(id=my_kahvalti)
    ogle_yemegi_program = Program.objects.get(id=my_ogle_yemegi)
    aksam_yemegi_program = Program.objects.get(id=my_aksam_yemegi)

    email_icerik = f"""
        <table border="1">
            <tr>
                <th>Kahvaltı Programı</th>
                <td>{kahvalti_program.icerik}</td>
            </tr>
            <tr>
                <th>Öğle Yemeği Programı</th>
                <td>{ogle_yemegi_program.icerik}</td>
            </tr>
            <tr>
                <th>Akşam Yemeği Programı</th>
                <td>{aksam_yemegi_program.icerik}</td>
            </tr>
        </table>

        Mesaj: {my_icerik}
        """
    
    form = ContactmeForm()
    if request.method == 'POST':
        form = ContactmeForm(request.POST)
        konu = my_konu
        icerik = email_icerik
        gonderen = my_gonderen
        alici=my_alici
        obj=ContactForm(
            name="Diyetisyen Merkezi",
            subject=my_konu,
            message=my_icerik,
            email=my_alici
        ) 
        try:
            obj.save()
            send_mail(
            subject=konu,
            message='',
            from_email='diyetisyenmerkezi12@gmail',  # Gönderen e-posta adresi
            recipient_list=[alici],
            html_message=email_icerik,
        )
            #send_mail(konu, icerik, gonderen, [alici])

            # Başarılı mesajı messages framework'ü ile ayarla
            messages.success(request, 'Mesajınız başarıyla gönderildi.')
            return render(request, 'kullanicilar.html', {'form': form})
        except Exception as e:
            # Hata durumunda mesajı messages framework'ü ile ayarla
            messages.error(request, f'Mesaj gönderilirken bir hata oluştu: {e}')
            return render(request, 'kullanicilar.html', {'form': form})
    return render(request, 'kullanicilar.html',{'form': form})
 
def yorumlar(request):
    
    yorumlar = Yorum.objects.all()
    form = YorumFormu()
    
    if request.method == 'POST':
        form = YorumFormu(request.POST)
        if form.is_valid():
            yeni_yorum = form.save(commit=False)
            yeni_yorum.kullanici = request.user
            yeni_yorum.save()
            return redirect('yorumlar')
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
    return render(request, 'index.html',data)

def email(request):
    data = {
       
        }
    return render(request, "mail_formu.html", data) 
def iletisim(request):
    data = {
       
        }
    return render(request, "iletisim.html", data)    
    
def prodetay(request):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        }
    return render(request, "prodetay.html", data)
def prodetay2(request):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        }
    return render(request, "prodetay2.html", data)
def prodetay3(request):
    data = {
        "yemekler": Food.objects.filter(anasayfa=True),
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        }
    return render(request, "prodetay3.html", data)

def prodetay4(request):
    data = {
        "kategoriler": Category.objects.all(),
        "yemekler": Food.objects.filter(anasayfa=True),
        }
    return render(request, "prodetay4.html", data)

def kullanici_listesi(request):
   
    data={
        "randevular" :Randevu.objects.filter(),
        "kullanici_listesi" :User.objects.filter(is_superuser=False),
        "yorumlar":Yorum.objects.filter(),
        "programlar":Program.objects.all()
    }
    
    
    return render(request, 'kullanicilar.html',data)


def yemekdetails(request, slug):
    data = {
        "yemek": Food.objects.get(slug=slug),
        "yorumlar" :Yorum.objects.all(),
        "form" :YorumFormu()
        }
   
   
    return render(request, "details.html", data)



@login_required(login_url='login')
def randevular(request):
    randevular = Randevu.objects.all()
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            randevu = form.save(commit=False)
            randevu.user = request.user
            randevu.save()

            
            # Send email to the selected doctor
            subject = 'Randevu Talebi'
            message = request.POST["mesaj"]
            from_email = 'diyetisyenmerkezi12@gmail.com'  # Use a valid sender email address
            to_email = randevu.doktor.email  # Assuming 'doktor' is a ForeignKey to a User model
        try:
            send_mail(subject, message, from_email, [to_email])
            
            messages.success(request, 'Randevu talebiniz gönderildi.')
            return render(request, 'randevu_al.html', {'form': form})
        except Exception as e:
            # Hata durumunda mesajı messages framework'ü ile ayarla
            messages.error(request, f'Randevu talebiniz gönderilirken bir hata oluştu: {e}')
            return render(request, 'randevu_al.html', {'form': form})

    return render(request, 'randevu_al.html', {'randevular': randevular, 'form': form})

def vucutkitle(request):
    return render(request, "partials/_vucut-kitle.html")

def bazal(request):
    return render(request, "partials/_bazal-metabolizma.html")

def vucutyag(request):
    return render(request, "partials/_vucut-yag.html")

def idealkilo(request):
    return render(request, "partials/_ideal-kilo.html")

def gunlukkalori(request):
    return render(request, "partials/_gunluk-kalori.html")

def diyetisyenler(request):
    return render(request, "diyetisyenler.html")
   
   
    