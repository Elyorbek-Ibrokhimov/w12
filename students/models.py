from django.db import models

class Maktab(models.Model):
    nomi = models.CharField(max_length=100, default='maktab')

    def __str__(self):
        return self.nomi

class Sinf(models.Model):
    nomi = models.CharField(max_length=100, default='sinf')
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, related_name='maktablar')

    def __str__(self):
        return self.nomi

class Student(models.Model):
    nomi = models.CharField(max_length=100, default='student')
    sinf = models.ForeignKey(Sinf, on_delete=models.CASCADE, related_name='studentlar')

    def __str__(self):
        return self.nomi
