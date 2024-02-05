from django.urls import path
from . import views as v

urlpatterns = [
    path('districtHome/', v.districtHome, name='districtHome'),
    path('districtInsert/', v.districtInsert, name='districtInsert'),
]