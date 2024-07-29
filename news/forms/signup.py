# news/forms/signup.py

from django import forms
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.save()
        return user