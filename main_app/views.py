from django.shortcuts import render, redirect
import requests

from settings_app.models import *
from service_app.models import ServiceCategory, Services
from .models import *
from news_app.models import News

# Source
def home_page(request):
    # Required
    seo_settings = SeoSettings.objects.last()
    site_settings = SiteSettings.objects.last()

    one_header = OneHeader.objects.all()
    two_header_titles = ServiceCategory.objects.all()
    two_header_services = Services.objects.all()

    footer_settings = FooterSettings.objects.last()
    footer_links = FooterLinks.objects.all()
    footer_address_info = FooterAddresInfo.objects.last()
    social_networks = SocialNetworks.objects.all()

    # Main
    home_welcome = HomeWelcome.objects.last()
    home_iqtibos = HomeIqtibos.objects.last()
    home_step = HomeStep.objects.last()
    home_services = HomeSerives.objects.filter(status=True)
    news = News.objects.all()
    home_counter = HomeCounter.objects.all()
    home_hamkorlar = HomeHamkor.objects.all()

    ctx = {
        # Required
        'seo_settings': seo_settings,
        'site_settings': site_settings,
        'one_header': one_header,
        'two_header_titles': two_header_titles,
        'two_header_services': two_header_services,
        'footer_settings': footer_settings,
        'footer_links': footer_links,
        'footer_address_info': footer_address_info,
        'social_networks': social_networks,

        # Main
        'home_welcome': home_welcome,
        'home_iqtibos': home_iqtibos,
        'home_step': home_step,
        'home_services_one': home_services[:3],
        'home_services_two': home_services[3:],
        'home_counter': home_counter,
        'home_hamkorlar': home_hamkorlar,
        'news': news,
    }

    return render(request, 'home-page.html', ctx)

def contact_page(request):
    TELEGRAM_BOT = TelegramBotSettings.objects.last()

    if request.method == "POST" and TELEGRAM_BOT:
        ContactRequests.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT.token}/sendMessage"

        payload = {
            "text": f"<b>✅ Yangi xabar:</b>\n\n"
                    f"<b>🧍‍♂️ Ism:</b> {request.POST['name']}\n"
                    f"<b>📞 Telefon raqami:</b> {request.POST['phone']}\n"
                    f"<b>◽️ Xabar:</b> {request.POST['message']}",
            "chat_id": TELEGRAM_BOT.user_id,
            "parse_mode": "HTML",
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
        return redirect('home_page')

    # Required
    seo_settings = SeoSettings.objects.last()
    site_settings = SiteSettings.objects.last()

    one_header = OneHeader.objects.all()
    two_header_titles = ServiceCategory.objects.all()
    two_header_services = Services.objects.all()

    footer_settings = FooterSettings.objects.last()
    footer_links = FooterLinks.objects.all()
    footer_address_info = FooterAddresInfo.objects.last()
    social_networks = SocialNetworks.objects.all()

    # Main
    contact_info = ContactInfo.objects.last()

    ctx = {
        # Required
        'seo_settings': seo_settings,
        'site_settings': site_settings,
        'one_header': one_header,
        'two_header_titles': two_header_titles,
        'two_header_services': two_header_services,
        'footer_settings': footer_settings,
        'footer_links': footer_links,
        'footer_address_info': footer_address_info,
        'social_networks': social_networks,

        # Main
        'contact_info': contact_info,
    }

    return render(request, 'contact.html', ctx)