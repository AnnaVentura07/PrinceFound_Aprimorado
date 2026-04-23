from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from cosmetics.views import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos-api', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/accounts/login/'), name='index'),
    path('', include('cosmetics.urls')), 
]