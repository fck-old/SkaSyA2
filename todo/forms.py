from django import forms

class NewForm(forms.Form):
    post = forms.CharField()