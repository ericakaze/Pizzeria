from django import forms
from .models import new_comment

class new_commentForm(forms.ModelForm):
    class Meta:
        model = new_comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
