from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register('api/product', ProductViewSet,'products')

urlpatterns = router.urls
