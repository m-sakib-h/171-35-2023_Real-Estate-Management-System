from django.urls import path, include
from rest_framework import routers

from . import api_view  #api_view ke import korlam

router = routers.DefaultRouter()   #router is a variable, routers class er ekta method ke call korlam r router diya inherit korlam
                                    #jehetu r kono route nai tai DefaultRouter a rakhlam
router.register(r'v1', api_view.RealtorViewSet)   # r holo raw string
                                                  #Route ta real hoba
urlpatterns = [
    path('', include(router.urls)),
]