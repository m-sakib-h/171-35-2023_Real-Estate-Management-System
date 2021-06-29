from rest_framework import viewsets   #viewset is a class behind the rest framework
from .serializers import ListingSerializer

from .models import Listing


class ListingViewSet(viewsets.ModelViewSet):        #object declare & inherit ModelViewSet
    queryset = Listing.objects.all().order_by('title')      #rest framework er vitora generic aca. generic er vitor a queryset aca ja bydefault Null kora thaka
                                                        #queryset override korlam
    serializer_class = ListingSerializer    #samevaba eitao override korbo
                                            #serializers.py theke niya aslam
