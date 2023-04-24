from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should start with a')




class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,required=True,validators=[check_for_a])
    age=forms.IntegerField()
