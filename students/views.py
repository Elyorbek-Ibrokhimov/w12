from django.shortcuts import render, get_object_or_404, redirect
from .models import Maktab, Sinf, Student
from .forms import MaktabForm, SinfForm, StudentForm

def maktab_list(request):
    maktablar = Maktab.objects.all()
    return render(request, 'school/maktab_list.html', {'maktablar': maktablar})

def maktab_detail(request, pk):
    maktab = get_object_or_404(Maktab, pk=pk)
    sinflar = Sinf.objects.filter(maktab=maktab)
    return render(request, 'school/maktab_detail.html', {'maktab': maktab, 'sinflar': sinflar})

def sinf_detail(request, pk):
    sinf = get_object_or_404(Sinf, pk=pk)
    studentlar = Student.objects.filter(sinf=sinf)
    return render(request, 'school/sinf_detail.html', {'sinf': sinf, 'studentlar': studentlar})

def sinf_create(request, maktab_pk):
    maktab = get_object_or_404(Maktab, pk=maktab_pk)
    if request.method == 'POST':
        form = SinfForm(request.POST)
        if form.is_valid():
            sinf = form.save(commit=False)
            sinf.maktab = maktab
            sinf.save()
            return redirect('maktab_detail', pk=maktab.pk)
    else:
        form = SinfForm()
    return render(request, 'school/sinf_form.html', {'form': form})

def sinf_edit(request, pk):
    sinf = get_object_or_404(Sinf, pk=pk)
    if request.method == 'POST':
        form = SinfForm(request.POST, instance=sinf)
        if form.is_valid():
            form.save()
            return redirect('sinf_detail', pk=pk)
    else:
        form = SinfForm(instance=sinf)
    return render(request, 'school/sinf_form.html', {'form': form})

def sinf_delete(request, pk):
    sinf = get_object_or_404(Sinf, pk=pk)
    if request.method == 'POST':
        sinf.delete()
        return redirect('maktab_detail', pk=sinf.maktab.pk)
    return render(request, 'school/sinf_confirm_delete.html', {'sinf': sinf})

def student_create(request, sinf_pk):
    sinf = get_object_or_404(Sinf, pk=sinf_pk)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.sinf = sinf
            student.save()
            return redirect('sinf_detail', pk=sinf.pk)
    else:
        form = StudentForm()
    return render(request, 'school/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('sinf_detail', pk=student.sinf.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'school/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        sinf_pk = student.sinf.pk
        student.delete()
        return redirect('sinf_detail', pk=sinf_pk)
    return render(request, 'school/student_confirm_delete.html', {'student': student})


def maktab_create(request):
    if request.method == 'POST':
        form = MaktabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maktab_list')
    else:
        form = MaktabForm()
    return render(request, 'school/maktab_form.html', {'form': form})

def maktab_edit(request, pk):
    maktab = get_object_or_404(Maktab, pk=pk)
    if request.method == 'POST':
        form = MaktabForm(request.POST, instance=maktab)
        if form.is_valid():
            form.save()
            return redirect('maktab_detail', pk=pk)
    else:
        form = MaktabForm(instance=maktab)
    return render(request, 'school/maktab_form.html', {'form': form})

def maktab_delete(request, pk):
    maktab = get_object_or_404(Maktab, pk=pk)
    if request.method == 'POST':
        maktab.delete()
        return redirect('maktab_list')
    return render(request, 'school/maktab_confirm_delete.html', {'maktab': maktab})