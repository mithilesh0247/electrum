from django.conf.urls import url,include
from rest_framework import routers
from testapp.api.views import MovieCRUDCBV
router=routers.DefaultRouter()
router.register('movieinfo',MovieCRUDCBV)
urlpatterns=[
url(r'',include(router.urls)),
]