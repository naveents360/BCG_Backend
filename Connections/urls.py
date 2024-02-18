from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet,AddressViewSet,ReviewerViewSet

connections_router = DefaultRouter()
connections_router.register('address',AddressViewSet)
connections_router.register('reviewers',ReviewerViewSet)
connections_router.register('application',ApplicationViewSet)
