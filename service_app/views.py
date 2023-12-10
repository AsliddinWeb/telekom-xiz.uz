from django.shortcuts import render
from django.shortcuts import get_object_or_404

from settings_app.models import *
from .models import ServiceCategory, Services, ServiceOrder
import requests

# Source
def service_home(request):
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

    }

    return render(request, 'service-home.html', ctx)

def service_detail(request, slug):
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
    service = get_object_or_404(Services, slug=slug)
    service_title = service.title

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
        'service': service,
    }

    TELEGRAM_BOT = TelegramBotSettings.objects.last()

    if request.method == "POST" and TELEGRAM_BOT:
        service_order = ServiceOrder.objects.create(
            service=service,
            name=request.POST['name'],
            phone=request.POST['phone'],
            address=request.POST['address'],
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT.token}/sendMessage"

        payload = {
            "text": f"<b>🎉 Yangi ariza:</b>\n\n"
                    f"<b>🛠 Ariza turi:</b> {service_title}\n\n"
                    f"<b>🧍‍♂️ Ism:</b> {request.POST['name']}\n"
                    f"<b>📞 Telefon raqami:</b> {request.POST['phone']}\n"
                    f"<b>🅰️ Manzil:</b> {request.POST['address']}",
            "chat_id": TELEGRAM_BOT.user_id,
            "parse_mode": "HTML",
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)

        ctx['service_order'] = service_order

        return render(request, 'service-success.html', ctx)

    return render(request, 'service-detail.html', ctx)