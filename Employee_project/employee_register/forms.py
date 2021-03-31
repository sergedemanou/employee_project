from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code'
        }
# les labels nous permettent de changer les noms de ces derniers car dans models que nous avons fait les noms seront ceux qui seront affichés

    def __init__(self,*args, **kwargs):
        super(EmployeeForm, self). __init__(*args, **kwargs)
        self.fields['position'].empty_label = 'select'
        self.fields['emp_code'].required = False     
        
# (self.fields['emp_code'].required = False)ici il n'y aura pas d'asterice sur ce champ
# cette partie nous permet d'avoir le mot "select" dans le dropdown de position
