from rest_framework import serializers
from .models import TaxSlab, Deduction, TaxPlan

class TaxSlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxSlab
        fields = '__all__'

class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = '__all__'

class TaxPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxPlan
        fields = '__all__'
