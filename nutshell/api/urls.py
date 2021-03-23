from django.conf.urls import include, url
from rest_framework import routers
from nutshell.api.views import ManufacturerViewSet, ShoeTypeViewSet, ShoeViewSet, ShoeColorViewSet

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'type', ShoeTypeViewSet)
router.register(r'color', ShoeColorViewSet)
router.register(r'shoe', ShoeViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]