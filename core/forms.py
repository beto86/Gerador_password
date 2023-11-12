from django import forms

class PasswordParameters(forms.Form):
    length = forms.ChoiceField(
        choices=[(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10')],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    uppercase = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
        )
    number = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
        )
    special = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
        )




