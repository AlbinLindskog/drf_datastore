from django.urls import path, include

import datastore.urls


urlpatterns = [
    path('datastore/', include('datastore.urls', namespace='datastore')),
]
