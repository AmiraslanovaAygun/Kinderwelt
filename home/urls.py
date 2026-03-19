from django.urls import path
from .views import  home_view


app_name = 'home'


urlpatterns = [
    path("", home_view, name='home'),
]


handler404 = 'home.views.custom_404_view'
handler500 = 'home.views.custom_500_view'
handler403 = 'home.views.custom_403_view'
handler503 = 'home.views.custom_503_view'