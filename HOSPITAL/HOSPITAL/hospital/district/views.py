from django.shortcuts import render
from division.models import Divisions
from district.models import Districts
# Create your views here.
def districtHome(request):
    retrieveDivision = Divisions.objects.all()
    context = {'dv': retrieveDivision}
    
    return render(request, 'division/dist.html', context)


def districtInsert(request):

    divisionID = request.POST.get('divisionID')
    districName = request.POST.get('districName')
    print(f"Division ID: {divisionID}")
    division =  Divisions.objects.get(id = divisionID)


    dist = Districts()

    dist.districName = districName
    dist.divisionID = division

    dist.save()

    return render(request, 'division/district.html')