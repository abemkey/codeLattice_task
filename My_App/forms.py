from django import forms

from My_App.models import Person


class Person_Form(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')