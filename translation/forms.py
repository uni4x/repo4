# translation/forms.py

from django import forms

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(label='Text to Translate', widget=forms.Textarea)