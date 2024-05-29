from django import forms
from .models import Region, District, School, Sinf

class LocationForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label="Doimiy ro'yxatdan o'tgan hudud")
    district = forms.ModelChoiceField(queryset=District.objects.none(), label="Doimiy ro'yxatdan o'tgan tuman(shahar)")
    school = forms.ModelChoiceField(queryset=School.objects.none(), label="Doimiy ro'yxatdan o'tgan maktab")
    sinf = forms.ModelChoiceField(queryset=Sinf.objects.none(), label="Sinf")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['district'].queryset = District.objects.none()
        else:
            self.fields['district'].queryset = District.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['school'].queryset = School.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['school'].queryset = School.objects.none()
        else:
            self.fields['school'].queryset = School.objects.none()

        if 'school' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['sinf'].queryset = Sinf.objects.filter(school_id=school_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['sinf'].queryset = Sinf.objects.none()
        else:
            self.fields['sinf'].queryset = Sinf.objects.none()
