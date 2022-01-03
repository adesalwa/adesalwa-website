from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
      class Meta:
            model = Artikel
            fields = ('judul', 'body', 'kategory')
            widgets = {
                  "judul" : forms.TextInput(
                        attrs={
                              'class': 'from-control',
                              'type' : 'text',
                              'placeholder':"Judul Artikel",
                              'required' : True
                        }),
                  "body" : forms.Textarea(
                        attrs={
                              'class': 'from-control',
                              'cols'  : '30',
                              'rows' : '10',
                              'required' : True
                        }),
                  "kategory" : forms.Select(
                        attrs={
                              'class': 'from-control selectpicker',
                              'type' : 'text',
                              'required' : True,
                              'data-style' : 'btn btn-danger btn-block',
                              'title' : 'pilih kategory', 
                              'data-size' : '7'
                        }),
            }