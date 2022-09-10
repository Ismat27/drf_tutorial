from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin,\
     UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
):
    queryset = Product.objects.all().order_by("?")
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class ProductMixins(
    ListModelMixin,
    CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args,**kwargs):
        return self.list(request, *args,**kwargs)

    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if not content:
            content = title
        serializer.save(content=content)

class SingleProductMixin(RetrieveModelMixin,
                        UpdateModelMixin,
                        DestroyModelMixin,
                        generics.GenericAPIView
                    ):
    queryset = Product.objects.all()
    lookup_field = 'pk'
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()
    
    def perform_destroy(self, instance):
        print('deleted')
        print(instance.title)

class RetrieveUpdateDelete(
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

    def perform_destroy(self, instance):
        print(f'{instance.title} deleted')
        return super().perform_destroy(instance)


