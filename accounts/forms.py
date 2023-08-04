from django import forms
from .models import Account

class MemberForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email','passwd']
