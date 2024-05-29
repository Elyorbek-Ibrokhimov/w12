from django.shortcuts import render
from .forms import LocationForm

def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Ma’lumotlarni saqlash yoki qayta ishlash
            pass
    else:
        form = LocationForm()
    return render(request, 'location_form.html', {'form': form})

from django.http import JsonResponse
from .models import District

def load_districts(request):
    region_id = request.GET.get('region')
    districts = District.objects.filter(region_id=region_id).order_by('name')
    return JsonResponse(list(districts.values('id', 'name')), safe=False)
