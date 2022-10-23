from rest_framework import serializers

class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product',
        lookup_field='pk'
    )

class RelatedProductSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=15,read_only=True)
    content = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        qs = obj.product_set.all()
        return RelatedProductSerializer(qs, many=True, context=self.context).data