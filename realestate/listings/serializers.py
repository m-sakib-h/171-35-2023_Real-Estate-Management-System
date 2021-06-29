# serializers for listings app

from rest_framework import serializers
from .models import Listing


# serializers for realtor
class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:     #oi class ta represent kora
        model = Listing
        # fields=['realtor','title','address','city','state','zipcode','description','price'....]
        fields = '__all__'  #Magic method (__all__) sob field ke ekbar a represent kora
