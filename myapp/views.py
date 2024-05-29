from django.shortcuts import render
from django.http import JsonResponse
from .forms import LocationForm
from .models import District, School, Sinf

def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Ma’lumotlarni saqlash yoki qayta ishlash
            pass
    else:
        form = LocationForm()
    return render(request, 'location_form.html', {'form': form})

def load_districts(request):
    region_id = request.GET.get('region')
    if region_id:
        districts = District.objects.filter(region_id=region_id).order_by('name')
    else:
        districts = District.objects.none()
    return JsonResponse(list(districts.values('id', 'name')), safe=False)

def load_schools(request):
    district_id = request.GET.get('district')
    if district_id:
        schools = School.objects.filter(district_id=district_id).order_by('name')
    else:
        schools = School.objects.none()
    return JsonResponse(list(schools.values('id', 'name')), safe=False)

def load_sinf(request):
    school_id = request.GET.get('school')
    if school_id:
        sinf = Sinf.objects.filter(school_id=school_id).order_by('name')
    else:
        sinf = Sinf.objects.none()
    return JsonResponse(list(sinf.values('id', 'name')), safe=False)
