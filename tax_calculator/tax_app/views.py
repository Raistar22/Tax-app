from rest_framework import viewsets
from .models import TaxSlab, Deduction, TaxPlan
from .serializers import TaxSlabSerializer, DeductionSerializer, TaxPlanSerializer

class TaxSlabViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaxSlab.objects.all()
    serializer_class = TaxSlabSerializer

class DeductionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deduction.objects.all()
    serializer_class = DeductionSerializer

class TaxPlanViewSet(viewsets.ModelViewSet):
    queryset = TaxPlan.objects.all()
    serializer_class = TaxPlanSerializer
