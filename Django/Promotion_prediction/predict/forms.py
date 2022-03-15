from django import forms
from predict.models import Employee




class GetEmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ['employeeId', 'age','avg_training_score', 'length_of_service', 'department', 'education',
                  'gender', 'recruitment_channel', 'no_of_trainings', 'previous_year_rating', 'awards_won']

        widgets = {
            'employeeId': forms.NumberInput(attrs={'placeholder':'3242'}),
            'age': forms.NumberInput(attrs={'placeholder':'34'}),
            'avg_training_score': forms.NumberInput(attrs={'placeholder':'84'}),
            'length_of_service': forms.NumberInput(attrs={'placeholder':'12'}),
            'education': forms.Select(attrs={'class': 'form-control','option':'All'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'previous_year_rating': forms.Select(attrs={'class': 'form-control'}),
            'no_of_trainings': forms.Select(attrs={'class': 'form-control'}),
            'recruitment_channel': forms.Select(attrs={'class': 'form-control'}),
            'awards_won': forms.Select(attrs={'class': 'form-control'}),

        }
