from django import forms

class CreateForm(forms.Form):
    title = forms.CharField(label='Post Title', max_length=50)
    detail = forms.CharField(label='Post Details', max_length=500, widget=forms.Textarea)