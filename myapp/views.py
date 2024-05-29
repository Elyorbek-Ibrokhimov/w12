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
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})




from django.shortcuts import render, redirect
from .forms import LocationForm, StudentForm

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)  # Bazaga saqlashdan oldin, sinfni o'zgartirish uchun ma'lumotlarni olish
            location_form = LocationForm(request.POST)
            if location_form.is_valid():
                region = location_form.cleaned_data['region']
                district = location_form.cleaned_data['district']
                school = location_form.cleaned_data['school']
                sinf = location_form.cleaned_data['sinf']
                # Bazaga saqlash
                student.save()
                return redirect('success')  # Agar muvaffaqiyatli saqlansa, success sahifasiga yo'naltirish
    else:
        student_form = StudentForm()
        location_form = LocationForm()
    return render(request, 'add_student.html', {'student_form': student_form, 'location_form': location_form})

def success(request):
    return render(request, 'success.html')


