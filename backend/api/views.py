from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def home(request, *args, **kwargs):
    if request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            # instance = serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "invalid data"}, status=400)
    instance = Product.objects.all().order_by("?")
    data = []
    if instance:
        # data = [ProductSerializer(item).data for item in instance]
        data = ProductSerializer(instance, many=True).data
    return Response(data)
