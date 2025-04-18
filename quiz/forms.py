from django import forms

class ImportWordForm(forms.Form):
    word_file = forms.FileField(label="Tải lên file Word (.docx)")
