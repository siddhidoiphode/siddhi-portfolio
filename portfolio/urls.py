"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

# from . import views
# # from django.config.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("",views.home),
# ] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('view_resume/', views.view_resume, name='view_resume'),
    path('emenuPresentation/', views.emenuPresentation, name='emenuPresentation'),
    path('emenuReport/', views.emenuReport, name='emenuReport'),
    path('webEmenu/', views.webEmenu, name='webEmenu'),
    path('webCarnival/',views.webCarnival , name='webCarnival'),
    path('webEcommerceSalesDashboard/', views.webEcommerceSalesDashboard, name='webEcommerceSalesDashboard'),
    path('SupermarketSalesDashboard/', views.SupermarketSalesDashboard, name='SupermarketSalesDashboard'),
    path('contact/', views.contact_view, name='contact'),
]



# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# from django.conf import settings
# print("ALLOWED_HOSTS at runtime =", settings.ALLOWED_HOSTS)
