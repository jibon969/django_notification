
from django import forms
from django.forms import Textarea
from .models import DeveloperDocument


class DateInput(forms.DateInput):
    input_type = 'date'


class DeveloperDocumentForm(forms.ModelForm):
    class Meta:
        model = DeveloperDocument
        fields = [
            'title',
            'file_type',
            'details',
            'file',
            'date',
            'approved'
        ]

        # Override the Customer some fields
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'details': Textarea(attrs={'rows': 4, 'cols': 4}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            max_size = 100 * 1024 * 1024  # 10 MB limit
            if file.size > max_size:
                raise forms.ValidationError('File size must be less than 10 MB.')
        return file