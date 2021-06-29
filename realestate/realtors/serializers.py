# serializers for realtors app
#serializers convert model instances to JSON so that the frontend can work with the received data.

from rest_framework import serializers
from .models import Realtor

class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:         #oi class ta represent kora
        model = Realtor
        # fields=['name','photo','desc','email','is_mvp','phone','message','contact_date']
        fields = '__all__'  #Magic method (__all__) sob field ke ekbar a represent kora
