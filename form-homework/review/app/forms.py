from django import forms
from .models import Review
import re


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    def clean_text(self):
        text = self.cleaned_data['text']
        text = text.replace("\'", "\'\'")
        return self.cleaned_data

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
