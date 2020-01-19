from django import forms


class Form(forms.Form):
    text = forms.IntegerField(min_value=0, max_value=100)

    def clean(self):
        return self.cleaned_data
