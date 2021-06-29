from django.urls import path, include
from rest_framework import routers

from . import views

from . import api_view   #api_view ke import korlam

router = routers.DefaultRouter()    #router is a variable, routers class er ekta method ke call korlam r router diya inherit korlam
                                    #jehetu r kono route nai tai DefaultRouter a rakhlam

router.register('v1', api_view.ListingViewSet)      # r holo raw string
                                                  #Route ta real hoba

urlpatterns = [
    path('listings/', views.listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('inquiry/', views.listing_inquiry, name='listing_inquiry'),
    path('',include(router.urls)),
]
