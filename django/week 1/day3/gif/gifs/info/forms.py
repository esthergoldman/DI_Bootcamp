from django import forms

class AddGif(forms.Form):
    uploader_name = forms.CharField()
    title = forms.CharField()
    url = forms.URLField()
    field_order = ['title','url','uploader_name'] # Sets order title,url,uploader_name	




