from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED


class PUTAsCreateMixin(object):
    """
    Mixin that adds PUT-as-create behaviour.

    This means that the frontend does not need to keep track of whether
    to create our update a resource, just put as you want it to look.
    """
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if instance is None:
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        try:
            return super().get_object()
        except (ObjectDoesNotExist, Http404):
            return None
