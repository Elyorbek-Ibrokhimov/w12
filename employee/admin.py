# admin.py
from django.contrib import admin
from .models import Viloyat, Tuman, Odam, Maktab, Manzil, Mahalla, Student

admin.site.register(Viloyat)
admin.site.register(Tuman)
admin.site.register(Odam)
admin.site.register(Maktab)
admin.site.register(Manzil)
admin.site.register(Mahalla)
admin.site.register(Student)


