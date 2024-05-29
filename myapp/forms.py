from django import forms
from .models import Region, District

class LocationForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label="Doimiy ro'yxatdan o'tgan hudud")
    district = forms.ModelChoiceField(queryset=District.objects.none(), label="Doimiy ro'yxatdan o'tgan tuman(shahar)")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['district'].queryset = District.objects.none()
        elif self.instance and self.instance.pk:
            self.fields['district'].queryset = self.instance.region.district_set.order_by('name')
        else:
            self.fields['district'].queryset = District.objects.none()