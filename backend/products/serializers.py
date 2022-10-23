from turtle import title
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from api.serializers import UserPublicSerializer


class RelatedProductSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=15,read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    product_discount = serializers.SerializerMethodField(read_only=True)
    # product_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='product',
    #     lookup_field='pk'
    # )
    class Meta:
        model = Product
        fields = [
            'owner',
            'id',
            # 'url',
            # 'product_url',
            'title',
            'content',
            'price',
            'sale_price',
            'product_discount',
        ]
    
    def validate_title(self, value):
        request = self.context.get('request')
        if request.method != 'POST':
            return value
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs:
            raise serializers.ValidationError('product with same title already exists')
        return value
    
    def get_product_discount(self, obj):
        if not hasattr(obj, 'id'): return None
        if not isinstance(obj, Product): return None
        return obj.get_discount()
    
    def get_product_url(self, obj):
        if not hasattr(obj, 'id'): return None
        if not isinstance(obj, Product): return None
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product', kwargs={'pk': obj.pk}, request=request)

    # def get_related_products(self, obj):
    #     qs = Product.objects.filter()