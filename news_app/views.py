from django.shortcuts import render
from django.shortcuts import get_object_or_404

from settings_app.models import *
from service_app.models import ServiceCategory, Services
from .models import News

def news_detail(request, slug):
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
    news = get_object_or_404(News, slug=slug)

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
        'news': news,
    }

    return render(request, 'news-detail.html', ctx)
