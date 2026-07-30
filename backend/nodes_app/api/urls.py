from django.urls import path, include
from rest_framework import routers
from nodes_app.api.views import NodeViewSet

router = routers.DefaultRouter()
router.register(r'nodes', NodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]