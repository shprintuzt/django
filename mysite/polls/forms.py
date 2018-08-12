from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'