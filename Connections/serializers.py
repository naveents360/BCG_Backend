from rest_framework.serializers import ModelSerializer,IntegerField,DateField
from .models import Address,Reviewer,Application

class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

class ReviewerSerializer(ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'

class ApplicationSerializer(ModelSerializer):
    reviewer_id = IntegerField(write_only=True,allow_null=True)
    address_id = IntegerField(write_only=True)    
    approval_date = DateField(allow_null=True)

    class Meta:
        model = Application
        fields = '__all__'
        depth = 1