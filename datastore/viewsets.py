from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from .mixins import PUTAsCreateMixin
from .models import DataStore
from .serializers import DataStoreSerializer


class DataStoreViewSet(RetrieveModelMixin, PUTAsCreateMixin, viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = DataStoreSerializer
    lookup_field = 'key'
    lookup_value_regex = '[^/]+'

    def get_queryset(self):
        return DataStore.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(key=self.kwargs[self.lookup_field], user=self.request.user)