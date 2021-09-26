from django.urls import path
from .views import HomePageView, AboutPageView,LoginPageView,RegesterPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('regester/', RegesterPageView.as_view(), name='regester'),
    path('', HomePageView.as_view(), name='home'),

]
