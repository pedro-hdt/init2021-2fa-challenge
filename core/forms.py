from django import forms

def validate_numerical(value):
    if not value.isdigit():
        raise forms.ValidationError(
            'The secret number should only include digits (0-9)')

class Layer2AuthForm(forms.Form):
    secret_number = forms.CharField(
        max_length=6, 
        min_length=6, 
        validators=[validate_numerical]
    )
