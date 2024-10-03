from django import forms
from .models import StudyMaterial

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['material_name', 'subject', 'author', 'date_uploaded', 'pdf_file']
