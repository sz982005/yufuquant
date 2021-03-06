from rest_framework import mixins
from rest_framework import viewsets

from .models import Exchange
from .serializers import ExchangeSerializer


class ExchangeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ExchangeSerializer

    def get_queryset(self):
        return Exchange.objects.all().order_by("-created_at")
