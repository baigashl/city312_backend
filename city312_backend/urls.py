"""city312_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema/', get_schema_view(title='API Schema'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(
          template_name='docs.html',
          extra_context={'schema_url': 'openapi-schema'}
      ), name='swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/user/', include('apps.users.urls')),
    path('api/discount/', include('apps.discount.urls')),
    path('api/activity_type/', include('apps.activity_type.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('api/review/', include('apps.review.urls')),
    path('rest-login/', include("rest_framework.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

