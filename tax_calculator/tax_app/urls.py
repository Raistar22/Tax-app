from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaxSlabViewSet, DeductionViewSet, TaxPlanViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'taxslabs', TaxSlabViewSet)
router.register(r'deductions', DeductionViewSet)
router.register(r'taxplans', TaxPlanViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes registered with the router
]
