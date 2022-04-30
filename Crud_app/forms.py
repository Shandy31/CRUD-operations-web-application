from django import forms
from .models import User

class Add_A_User(forms.ModelForm):
    class Meta:
        model = User
        fields = ['patient_name', 'gender', 'age', 'phone_no', 'DR_preferred']