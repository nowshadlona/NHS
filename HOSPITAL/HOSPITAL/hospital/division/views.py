from django.shortcuts import redirect, render
# from django.http import HttpResponse
from .models import Divisions




# Create your views here.


def divisionHome(request):
    return render(request, 'division/divis.html')



def divisionInsert(request):
    divisionName = request.POST.get('divisionName')

    division = Divisions()

    division.divisionName = divisionName
    division.save()


    return redirect('divisionHome')

