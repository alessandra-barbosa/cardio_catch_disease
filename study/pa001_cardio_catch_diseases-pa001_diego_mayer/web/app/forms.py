from django import forms
from .models import Patients

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patients
        fields = ('id', 'name', 'age', 'gender', 'height', 'weight', 'hight_pressure', 'low_pressure', 
                  'cholesterol', 'glucose', 'smoker', 'alcohol', 'active', 'cardio')