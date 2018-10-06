from rest_framework import routers

from .views import TitleViewSet, NameViewSet

router = routers.DefaultRouter()
router.register(r'title', TitleViewSet)
router.register(r'name', NameViewSet)
