from django.contrib import admin
from django.utils.html import format_html
from .models import  HomeSwiper, HomeProducts, HomeProductsTitle, HomeAbout, HomeSortiment, HomeContact, Gallery

# Register your models here.

@admin.register(HomeSwiper)
class HomeSwiperAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    ordering = ('order',)


    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'

@admin.register(HomeProductsTitle)
class HomeProductsTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(HomeProducts)
class HomeProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'


@admin.register(HomeAbout)
class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    list_editable = ( 'is_active',)
    search_fields = ('title', 'description',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'


@admin.register(HomeSortiment)
class HomeSortimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'


@admin.register(HomeContact)
class HomeContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'email', 'image_preview')
    search_fields = ('address', 'phone_number', 'email')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'order', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('image_title',)
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Preview'