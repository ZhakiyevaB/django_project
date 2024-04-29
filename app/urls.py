""" app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) """

from django.contrib import admin
from django.urls import include, path, re_path 
from django.conf.urls.static import static
from app import settings
from app.settings import DEBUG

from users.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/', include('api.urls')),
    path('api/v1/userzlist/', UserzAPIView.as_view()),
    path('api/v1/userzlist/<int:pk>/', UserzAPIView.as_view()),
    path('api/v1/userz/', UserzAPIList.as_view()),
    path('api/v1/userz/<int:pk>/', UserzAPIUpdate.as_view()),
    path('api/v1/userzdelete/<int:pk>/', UserzAPIDestroy.as_view()),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
     path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG: 
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),        
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


"""
www.site.com.admin
www.site.com
www.site.com/about/
www.ste.com/catalog/
www.site.catalog/product
"""