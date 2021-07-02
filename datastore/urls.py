from rest_framework import routers

from .viewsets import DataStoreViewSet


app_name = 'datastore'

router = routers.SimpleRouter()

router.register('', DataStoreViewSet, basename='datastore')

urlpatterns = router.urls