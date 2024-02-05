from django.urls import path
from . import views as v
urlpatterns = [
    path('', v.divisionHome, name='divisionHome'),
    path('divisionInsert/', v.divisionInsert, name='divisionInsert'),
]