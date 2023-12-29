from django.urls import path
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from api.views import EmployeeModelViewSetView
router.register("v2/employees",EmployeeModelViewSetView,basename="memployees")

urlpatterns=[
    
] + router.urls