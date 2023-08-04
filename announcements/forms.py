from django import forms
from .models import Announcement

class MemberForm(forms.ModelForm):
    class Meta:
        model = Announcement 
        fields = ['title','passwd','email','club','message']
