from django import forms

class ExampleForm(forms.Form):
    book_title = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)