from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer 