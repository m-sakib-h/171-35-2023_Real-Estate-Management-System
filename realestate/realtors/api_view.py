from rest_framework import viewsets  #viewset is a class behind the rest framework
from .serializers import RealtorSerializer

from .models import Realtor


class RealtorViewSet(viewsets.ModelViewSet):    #object declare & inherit ModelViewSet
    queryset = Realtor.objects.all().order_by('name')   #rest framework er vitora generic aca. generic er vitor a queryset aca ja bydefault Null kora thaka
                                                        #queryset override korlam
    serializer_class = RealtorSerializer    #samevaba eitao override korbo
                                            #serializers.py theke niya aslam
