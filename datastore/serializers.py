from rest_framework import serializers

from .models import DataStore


class DataStoreSerializer(serializers.ModelSerializer):
    """
    Simple serializer that simply maps all incoming data to
    the 'data' field on the DataStore model.
    """

    data = serializers.JSONField(required=True)

    class Meta:
        model = DataStore
        fields = ('data', )

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs:
            kwargs['data'] = {'data': kwargs['data']}
        super().__init__(*args, **kwargs)

    @property
    def data(self):
        ret = super().data['data'] or {}
        return serializers.ReturnDict(ret, serializer=self)
