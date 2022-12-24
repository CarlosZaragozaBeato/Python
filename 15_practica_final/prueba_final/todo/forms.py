from django.forms import ModelForm, DateInput
from .models import Todo
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets ={
            'estimated_date':DateInput(attrs={'type':'date'})
        } 
        