from django.shortcuts import render
from .models import Gallery, HomeProductsTitle, HomeSwiper, HomeProducts, HomeAbout, HomeSortiment, HomeContact


def home_view(request):
    home_products_title = HomeProductsTitle.objects.first()
    swiper_images = HomeSwiper.objects.filter(is_active=True).order_by('order')
    home_products = HomeProducts.objects.filter(is_active=True).order_by('order')
    home_abouts = HomeAbout.objects.filter(is_active=True).all()
    home_sortiments = HomeSortiment.objects.filter(is_active=True).order_by('order')
    home_contact = HomeContact.objects.first()
    gallery_images = Gallery.objects.filter(is_active=True).order_by('order')

    context = {
        'swiper_images': swiper_images,
        'home_products': home_products,
        'home_abouts': home_abouts,
        'home_products_title': home_products_title,
        'home_sortiments': home_sortiments,
        'home_contact': home_contact,
        'gallery_images': gallery_images,
    }
    return render(request, 'home.html', context)





def custom_404_view(request):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

def custom_403_view(request):
    return render(request, '403.html', status=403)

def custom_503_view(request):
    return render(request, '503.html', status=503)