
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginPage,name="naradMuni_login"),
    path('signup-page/',views.signUpPage,name="naradMuni_signup"),
    path('dashboard-page/', views.dash, name="naradMuni_dashboard"),
    path("Today-News/",views.getNews,name="naradMuni_news"),
    path('contact-us/',views.contactusPage,name="naradMuni_contactus"),
    path("logout/",views.logoutPage,name="naradMuni_logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

