from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__()
            
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input', 'placeholder': f'Add {field.label}'})
                