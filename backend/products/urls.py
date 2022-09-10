from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView,\
    ProductUpdateAPIView, ProductDeleteAPIView, ProductMixins,\
    SingleProductMixin, RetrieveUpdateDelete

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    # path('', ProductMixins.as_view()),
    # path('<int:pk>/', SingleProductMixin.as_view()),
    path('<int:pk>/', RetrieveUpdateDelete.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view()),
]