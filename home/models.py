from django.db import models

# Create your models here.

class HomeSwiper(models.Model):
    image = models.ImageField(
        upload_to='home_swiper/',
        help_text="Image to be displayed in the home page swiper"
    )
    title = models.CharField(
        max_length=200,
        help_text="Title for the swiper image"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order of the image in the swiper"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this image is active and should be displayed"
    )

    def __str__(self):
        return f"Swiper Image {self.order} - {'Active' if self.is_active else 'Inactive'}"

    class Meta:
        ordering = ['order']
        verbose_name = "Home Swiper Image"
        verbose_name_plural = "Home Swiper Images"

class HomeProductsTitle(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Title to be displayed in the home page"
    )
    description = models.TextField(
        help_text="Description to be displayed in the home page"
    )

    def __str__(self):
        return f"Home Title - {self.title}"


class HomeProducts(models.Model):
    image = models.ImageField(
        upload_to='home_products/',
        help_text="Image to be displayed in the home page products section"
    )
    title = models.CharField(
        max_length=200,
        help_text="Title for the product image"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order of the image in the home products section"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this image is active and should be displayed"
    )

    def __str__(self):
        return f"Product Image {self.order} - {'Active' if self.is_active else 'Inactive'}"
    class Meta:
        ordering = ['order']
        verbose_name = "Home Product Image"
        verbose_name_plural = "Home Product Images"



class HomeAbout(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Title for the about section"
    )
    description = models.TextField(
        help_text="Description for the about section"
    )
    image = models.ImageField(
        upload_to='home_about/',
        help_text="Image to be displayed in the about section"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this about section is active and should be displayed"
    )

    def __str__(self):
        return f"About Section - {'Active' if self.is_active else 'Inactive'}"

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"


class HomeSortiment(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Title for the sortiment item"
    )
    image = models.ImageField(
        upload_to='home_sortiment/',
        help_text="Image to be displayed for the sortiment item"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order of the sortiment item in the list"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this sortiment item is active and should be displayed"
    )

    def __str__(self):
        return f"Sortiment Item {self.order} - {'Active' if self.is_active else 'Inactive'}"

    class Meta:
        ordering = ['order']
        verbose_name = "Sortiment Item"
        verbose_name_plural = "Sortiment Items"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    image_title = models.CharField(
        max_length=200,
        help_text="Title for the gallery image"
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)


    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"Gallery Image {self.id}"

class HomeContact(models.Model):
    address = models.CharField(
        max_length=255,
        help_text="Address to be displayed in the contact section"
    )
    phone_number = models.CharField(
        max_length=20,
        help_text="Phone number to be displayed in the contact section"
    )
    email = models.EmailField(
        help_text="Email to be displayed in the contact section"
    )
    image = models.ImageField(
        upload_to='home_contact/',
        help_text="Image to be displayed in the contact section"
    )
    footer_text = models.TextField(
        blank=True,
        null=True,
        help_text="Text to be displayed in the footer section"
    )
    map_url = models.TextField(
    blank=True,
    null=True,
    help_text="Paste the Google Maps iframe src URL here (only the value inside the src attribute)."
    )

    owner_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Name of the owner to be displayed in the contact section"
    )

    instagram_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the Instagram profile to be displayed in the contact section"
    )
    facebook_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the Facebook profile to be displayed in the contact section"
    )
    tiktok_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the TikTok profile to be displayed in the contact section"
    )
    whatsapp_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the WhatsApp contact to be displayed in the contact section"
    )
    pinterest_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to the Pinterest profile to be displayed in the contact section"
    )

    def __str__(self):
        return f"Contact Information - {self.address}"

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"