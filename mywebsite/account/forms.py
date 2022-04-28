# this fucking form
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# this is useless fucking form
class formLogin(AuthenticationForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(formLogin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'pl-8 border-b-2 outline-none focus:border-primarycolor duration-500'
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'pl-8 border-b-2 outline-none focus:border-primarycolor duration-500','placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'class':'pl-8 border-b-2 outline-none focus:border-primarycolor duration-500','placeholder':'Password'})
          }         

class formRegister(UserCreationForm):
    fields=['username','email','password1','password2']
    