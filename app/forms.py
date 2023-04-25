from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should not start with a')




class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,required=True,validators=[check_for_a])
    age=forms.IntegerField()
    Email=forms.EmailField()
    re_enter_Email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher'] 
        if len(bot)>0:
           raise forms.ValidationError('bot')