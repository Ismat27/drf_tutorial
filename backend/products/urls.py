from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView,\
    ProductUpdateAPIView, ProductDeleteAPIView, ProductMixins,\
    SingleProductMixin, RetrieveUpdateDelete, _api

urlpatterns = [
    path('', ProductMixins.as_view()),
    # path('<int:pk>/', SingleProductMixin.as_view()),
    path('<int:pk>/', RetrieveUpdateDelete.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view()),
    path('<int:pk>/test/', _api)
]