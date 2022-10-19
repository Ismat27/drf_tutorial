from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSets

router = DefaultRouter()
router.register('products', ProductViewSets, basename='products')

urlpatterns = router.urls