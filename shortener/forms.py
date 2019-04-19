from django import forms
from .validators import validate_url, validate_dot_com

class SubmitURLForm(forms.Form):
    url = forms.CharField(
    label = '',
    validators=[validate_url,validate_dot_com],
    widget= forms.TextInput(
            attrs = {
                "placeholder": "Long URL",
                "class": "form-control"
            }
    )
    )

    # def clean(self):
    #     cleaned_data = super(SubmitURLForm,self).clean()
    #     url = cleaned_data['url']
    #     print(url)
    #
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     print(url)
    #     return url
